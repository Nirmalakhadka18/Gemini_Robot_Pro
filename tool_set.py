import os
import shutil
import platform
import fnmatch
from typing import List, Dict

def get_system_info() -> str:
    """Returns a summary of the current system."""
    uname = platform.uname()
    return f"System: {uname.system} {uname.release} ({uname.version})\nNode: {uname.node}\nMachine: {uname.machine}"

def find_files(pattern: str, search_path: str = ".") -> List[str]:
    """
    Recursively finds files matching a glob pattern (e.g., '*.pdf').
    
    Args:
        pattern: The glob pattern to match.
        search_path: The root directory to start searching from. Defaults to current directory.
        
    Returns:
        A list of absolute paths to matching files.
    """
    matches = []
    # Normalize path
    search_path = os.path.abspath(search_path)
    
    # Safety check: Prevent searching entire C: drive implicitly if users just say "find pdfs"
    # But if user explicitly asks for C:, we allow it (though it might be slow).
    # We will trust the caller (LLM/Main) to warn the user about scope.
    
    try:
        for root, dirnames, filenames in os.walk(search_path):
            # Filter matches in current directory
            for filename in fnmatch.filter(filenames, pattern):
                matches.append(os.path.join(root, filename))
    except PermissionError:
        pass # Skip folders we can't access
        
    return matches

def move_files(source_paths: List[str], destination_folder: str) -> Dict[str, str]:
    """
    Moves a list of files to a destination folder.
    
    Args:
        source_paths: List of absolute file paths to move.
        destination_folder: Target directory.
        
    Returns:
        Dict with 'success' list and 'error' list.
    """
    results = {"success": [], "error": []}
    
    # Ensure destination exists
    destination_folder = os.path.abspath(destination_folder)
    if not os.path.exists(destination_folder):
        try:
            os.makedirs(destination_folder)
        except OSError as e:
            return {"success": [], "error": [f"Could not create destination {destination_folder}: {e}"]}

    for src in source_paths:
        try:
            if not os.path.exists(src):
                results["error"].append(f"Source not found: {src}")
                continue
                
            filename = os.path.basename(src)
            dest = os.path.join(destination_folder, filename)
            
            # Handle collision? For now, standard move (might overwrite or fail depending on OS)
            shutil.move(src, dest)
            results["success"].append(src)
        except Exception as e:
            results["error"].append(f"Failed to move {src}: {e}")
            
    return results

def copy_files(source_paths: List[str], destination_folder: str) -> Dict[str, str]:
    """
    Copies a list of files to a destination folder.
    """
    results = {"success": [], "error": []}
    
    destination_folder = os.path.abspath(destination_folder)
    if not os.path.exists(destination_folder):
        try:
            os.makedirs(destination_folder)
        except OSError as e:
            return {"success": [], "error": [f"Could not create destination {destination_folder}: {e}"]}

    for src in source_paths:
        try:
            if not os.path.exists(src):
                results["error"].append(f"Source not found: {src}")
                continue
                
            shutil.copy2(src, destination_folder)
            results["success"].append(src)
        except Exception as e:
            results["error"].append(f"Failed to copy {src}: {e}")
            
    return results

def get_tools_definition():
    """Returns the JSON schema for these tools to be passed to the LLM."""
    return [
        {
            "type": "function",
            "function": {
                "name": "find_files",
                "description": "Recursively find files matching a pattern in a directory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pattern": {
                            "type": "string",
                            "description": "Glob pattern (e.g., '*.pdf', 'notes.txt')."
                        },
                        "search_path": {
                            "type": "string",
                            "description": "Root directory to search. Default is '.'."
                        }
                    },
                    "required": ["pattern"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "move_files",
                "description": "Move a list of specific files to a destination folder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_paths": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of absolute paths of files to move."
                        },
                        "destination_folder": {
                            "type": "string",
                            "description": "Target directory path."
                        }
                    },
                    "required": ["source_paths", "destination_folder"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "copy_files",
                "description": "Copy a list of specific files to a destination folder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_paths": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of absolute paths of files to copy."
                        },
                        "destination_folder": {
                            "type": "string",
                            "description": "Target directory path."
                        }
                    },
                    "required": ["source_paths", "destination_folder"]
                }
            }
        }
    ]

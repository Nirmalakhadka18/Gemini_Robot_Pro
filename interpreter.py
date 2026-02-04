import json
import tool_set

def execute_tool_call(tool_call):
    """
    Executes a single tool call dictionary.
    
    Args:
        tool_call (dict): The tool call object from the LLM response.
                          Expected format: {'function': {'name': '...', 'arguments': '...'}}
    
    Returns:
        The result of the function execution.
    """
    function_name = tool_call['function']['name']
    try:
        arguments = json.loads(tool_call['function']['arguments'])
    except json.JSONDecodeError:
        return f"Error: Invalid JSON arguments for function {function_name}"

    if hasattr(tool_set, function_name):
        func = getattr(tool_set, function_name)
        try:
            # We assume arguments match the function signature. 
            # In a robust app, we might inspect signature or use **arguments
            return func(**arguments)
        except Exception as e:
            return f"Error executing {function_name}: {str(e)}"
    else:
        return f"Error: Unknown tool '{function_name}'"

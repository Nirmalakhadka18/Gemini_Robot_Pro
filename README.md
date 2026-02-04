# 🤖 Gemini Robot Pro

<div align="center">

**An Intelligent CLI-Based File Management Assistant Powered by Google Gemini**

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

*Transform natural language commands into powerful file system operations*

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Available Tools](#-available-tools)
- [Building Executable](#-building-executable)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**Gemini Robot Pro** is a sophisticated command-line interface (CLI) tool that leverages the power of Google's Gemini LLM to provide intelligent file management capabilities. Simply describe what you want to do in natural language, and let the AI handle the complex file operations.

Perfect for:
- 📁 Organizing large file collections
- 🚀 Automating repetitive file tasks
- 🔍 Finding files with advanced search capabilities
- 📝 Creating files and code through natural language
- ⚙️ Running system commands safely

---

## ✨ Features

### 🗣️ Natural Language Interface
- Communicate with your file system using plain English
- No need to memorize complex command syntax
- Context-aware responses and suggestions

### 🛠️ Powerful Tool Suite
- **`find_files`**: Recursive file search with advanced pattern matching
- **`move_files`**: Bulk file moving operations with safety checks
- **`copy_files`**: Duplicate files with confirmation prompts
- **`write_file`**: Create and modify files, generate code/websites
- **`run_terminal_command`**: Execute Git operations and system commands

### 🎨 Rich Terminal Experience
- Beautiful CLI interface with syntax highlighting
- Formatted panels and markdown rendering
- Colorful status messages and progress indicators
- Clear error messages and debugging information

### 🛡️ Safety & Security
- ✅ Confirmation prompts before destructive operations
- ✅ Secure API key management via environment variables
- ✅ Comprehensive error handling and logging
- ✅ Read-only operations by default

### 📦 Portable Distribution
- Build standalone Windows executable (.exe)
- No Python installation required for end users
- Easy deployment and sharing

---

## 🚀 Installation

### Prerequisites

- **Python 3.7+** installed on your system
- **OpenRouter API Key** - [Get your free API key](https://openrouter.ai)

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Nirmalakhadka18/Gemini_Robot_Pro.git
   cd Gemini_Robot_Pro
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   
   Create a `.env` file in the project root directory:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

5. **Verify Installation**
   ```bash
   python verify_api.py
   ```

---

## 💡 Usage

### Starting the CLI

```bash
python main.py
```

### Example Commands

Once the application starts, you can use natural language commands like:

```
📁 "Find all Python files in this directory"
🚚 "Move all .jpg files from Downloads to Pictures"
📄 "Create a new folder called ProjectFiles"
🌐 "Write a simple HTML page about coffee"
⚙️ "Run git status command"
🔍 "Search for all PDF files larger than 5MB"
📋 "Copy all Excel files to Backup folder"
```

### Interactive Workflow

1. **Enter your command** in natural language
2. **Review the AI's plan** - The assistant shows what it will do
3. **Confirm or cancel** - You approve before any action is taken
4. **See the results** - Clear feedback on operation success/failure

### Exiting the Application

Type `exit` or `quit` to safely close the application, or press `Ctrl+C`.

---

## 📁 Project Structure

```
Gemini_Robot_Pro/
├── main.py              # 🎯 Main CLI entry point and interactive loop
├── llm_client.py        # 🤖 OpenRouter API integration and response parsing
├── interpreter.py       # ⚙️ Tool call executor and command interpreter
├── tool_set.py          # 🔧 Tool definitions and function implementations
├── verify_api.py        # ✅ API connection verification script
├── list_models.py       # 📋 Available LLM models lister
├── test_tools.py        # 🧪 Tool testing and validation suite
├── requirements.txt     # 📦 Python package dependencies
├── GeminiRobot.spec     # 📦 PyInstaller build configuration
├── .env                 # 🔑 API keys and environment configuration
├── build/               # 🏗️ Build artifacts and temporary files
└── dist/                # 📦 Compiled executable output directory
```

### Key Files Description

| File | Purpose |
|------|---------|
| `main.py` | Entry point, handles user interaction and main loop |
| `llm_client.py` | Manages API calls to OpenRouter/Gemini LLM |
| `interpreter.py` | Executes tool calls returned by the LLM |
| `tool_set.py` | Defines available tools and their implementations |
| `verify_api.py` | Tests API connectivity and configuration |
| `list_models.py` | Lists available LLM models from OpenRouter |
| `test_tools.py` | Contains unit tests for tool functions |

---

## 🔧 Available Tools

### File Operations

| Tool | Description | Example Use |
|------|-------------|-------------|
| `find_files` | Search for files recursively | "Find all .docx files in Documents" |
| `move_files` | Move files to a destination | "Move all images to Photos folder" |
| `copy_files` | Copy files to a destination | "Copy all PDFs to Backup" |

### Content Creation

| Tool | Description | Example Use |
|------|-------------|-------------|
| `write_file` | Create or modify files | "Create index.html with basic structure" |

### System Commands

| Tool | Description | Example Use |
|------|-------------|-------------|
| `run_terminal_command` | Execute shell commands | "Run git pull" |

---

## 📦 Building Executable

Create a standalone Windows executable that doesn't require Python installation:

### Using Python Build Script

```bash
python GeminiRobot.spec
```

Or with PyInstaller directly:

```bash
pyinstaller --onefile --name=GeminiRobot main.py
```

### Output

The executable will be created in the `dist/` directory:
- **File**: `dist/GeminiRobot.exe`
- **Size**: ~10-15 MB (includes Python runtime)
- **Requires**: No Python installation on target machine

### Distribution

Simply copy `GeminiRobot.exe` to any Windows machine. Make sure to include a `.env` file with the API key in the same directory.

---

## ⚙️ Configuration

### Environment Variables

Configure the application by creating a `.env` file:

```env
# Required: OpenRouter API Key
OPENROUTER_API_KEY=sk-or-v1-xxxxx

# Optional: Default model (uncomment to customize)
# DEFAULT_MODEL=google/gemini-pro

# Optional: API timeout in seconds
# API_TIMEOUT=30
```

### Available Models

To see all available models:

```bash
python list_models.py
```

---

## 🐛 Troubleshooting

### Common Issues

#### ❌ API Key Error

**Problem**: `Error: OPENROUTER_API_KEY is not set`

**Solution**:
```bash
# Verify .env file exists and contains your API key
python verify_api.py
```

#### ❌ Module Not Found

**Problem**: `ModuleNotFoundError: No module named 'xxx'`

**Solution**:
```bash
# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

#### ❌ API Connection Failed

**Problem**: API requests timing out or failing

**Solution**:
1. Check your internet connection
2. Verify API key is valid at [openrouter.ai](https://openrouter.ai)
3. Run verification: `python verify_api.py`

#### ❌ Permission Denied

**Problem**: Cannot move/copy files

**Solution**:
- Ensure you have write permissions for target directories
- Run terminal/command prompt as administrator (Windows)
- Check if files are not in use by another application

### Debug Mode

To see detailed logs, check the `error.log` file in the project directory.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help improve Gemini Robot Pro:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Make your changes**
   - Add new tools in `tool_set.py`
   - Improve error handling
   - Add documentation
   - Fix bugs
4. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
6. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Test your changes with `test_tools.py`
- Update documentation as needed

---

## 📜 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Gemini Robot Pro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📧 Contact & Support

- **GitHub**: [@Nirmalakhadka18](https://github.com/Nirmalakhadka18)
- **Repository**: [Gemini_Robot_Pro](https://github.com/Nirmalakhadka18/Gemini_Robot_Pro)
- **Issues**: [Report a bug or request a feature](https://github.com/Nirmalakhadka18/Gemini_Robot_Pro/issues)

---

## 🙏 Acknowledgments

- **Google Gemini** - For the powerful LLM capabilities
- **OpenRouter** - For providing free API access
- **Rich** - For the beautiful terminal UI library
- **Python Community** - For the amazing ecosystem

---

## 🔮 Future Enhancements

Planned features for upcoming releases:

- [ ] 🌐 Multi-language support
- [ ] 📊 File analytics and reporting
- [ ] 🔄 Batch processing with progress bars
- [ ] 📝 Custom tool creation interface
- [ ] 🎨 GUI version with web interface
- [ ] 🔌 Plugin system for extensibility
- [ ] 📱 Mobile companion app
- [ ] ☁️ Cloud storage integration

---

<div align="center">

**Version 1.0.0** | Made with ❤️ using Python and Google Gemini AI

</div>

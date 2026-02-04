# 🤖 Gemini Robot Pro

<div align="center">

**An Intelligent CLI-Based File Management Assistant**

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Powered by](https://img.shields.io/badge/Powered%20by-Google%20Gemini-orange.svg)](https://deepmind.google/technologies/gemini/)

Transform natural language commands into powerful file system operations - no complex scripting required!

</div>

---

## ✨ Features

- **🗣️ Natural Language Control**: Simply describe what you need - "Find all PDFs in C: and move them to Desktop/PDFs"
- **🔧 Powerful Tool Suite**:
  - `find_files`: Recursive file search with pattern matching
  - `move_files` & `copy_files`: Bulk file operations with safety confirmations
  - `write_file`: Create and modify files, generate code and websites
  - `run_terminal_command`: Execute Git operations and system commands
- **🎨 Rich CLI Interface**: Beautiful terminal UI with syntax highlighting, panels, and markdown rendering
- **🛡️ Safety First**: Confirmation prompts before executing any destructive operations
- **📦 Portable**: Build as standalone Windows executable (.exe) for easy distribution

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- OpenRouter API key ([Get free API key at openrouter.ai](https://openrouter.ai))

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Nirmalakhadka18/Gemini_Robot_Pro.git
   cd Gemini_Robot_Pro
   ```

2. **Set Up Virtual Environment** (Recommended)
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   
   Create a `.env` file in the project root:
   ```env
   OPENROUTER_API_KEY=your_api_key_here
   ```

---

## 💡 Usage

### Running the CLI

```bash
python main.py
```

### Example Commands

Once the CLI starts, try these natural language commands:

```
📁 Find all Python files in this directory
🚚 Move all images from Downloads to Pictures folder
🌐 Create a simple HTML website about coffee
⚙️ Run git status command
📄 Copy all PDF files to a new folder called Documents
```

### Building Executable

Create a standalone Windows executable:

```bash
# Using batch script
build_exe.bat

# Or using Python script  
python build_exe.py
```

The executable will be available in `dist/GeminiRobot.exe`

---

## 📁 Project Structure

```
Gemini_Robot_Pro/
├── main.py              # CLI entry point and main loop
├── llm_client.py        # OpenRouter/Gemini API integration
├── interpreter.py       # Tool call executor and handler
├── tool_set.py          # Available tools and function definitions
├── verify_api.py        # API connection tester
├── list_models.py       # List available models
├── test_tools.py        # Tool testing suite
├── requirements.txt     # Python dependencies
├── build_exe.bat        # Windows build script
├── GeminiRobot.spec     # PyInstaller configuration
└── .env                 # API key configuration (create this)
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python** | Core programming language |
| **OpenRouter API** | Access to Google Gemini LLM |
| **Rich** | Beautiful terminal UI and formatting |
| **PyInstaller** | Executable packaging |
| **python-dotenv** | Environment variable management |
| **Requests** | HTTP client for API calls |

---

## 🔒 Security & Safety

- ✅ **Confirmation Required**: All file operations require explicit user approval
- ✅ **API Key Protection**: Keys stored in `.env` file (gitignored by default)
- ✅ **Error Handling**: Comprehensive error messages and logging
- ✅ **Safe Defaults**: Read-only operations prioritized, destructive actions confirmed

---

## 🐛 Troubleshooting

### API Key Issues
```bash
# Verify your API key is configured correctly
python verify_api.py
```

### Module Not Found
```bash
# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

### Executable Not Working
- Ensure you're running the build script from the project root directory
- Check that PyInstaller is installed: `pip install pyinstaller`
- Review build logs in the `build/` directory

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

---

## 📜 License

This project is open source and available under the **MIT License**.

---

## 📧 Contact & Support

- **GitHub**: [@Nirmalakhadka18](https://github.com/Nirmalakhadka18)
- **Repository**: [Gemini_Robot_Pro](https://github.com/Nirmalakhadka18/Gemini_Robot_Pro)
- **Issues**: [Report a bug or request a feature](https://github.com/Nirmalakhadka18/Gemini_Robot_Pro/issues)

---

<div align="center">

**Made with ❤️ using Google Gemini AI**

⭐ Star this repo if you find it helpful!

</div>

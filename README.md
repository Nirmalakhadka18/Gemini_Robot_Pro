# Gemini Robot Pro

Gemini Robot Pro is a smart CLI-based file management assistant powered by Google's Gemini LLM. It allows you to perform file system operations (like finding, moving, and copying files) using natural language commands.

## Features

- **Natural Language Control**: Just tell the robot what to do.
- **Tools**:
  - `find_files`: Recursive search.
  - `move_files` & `copy_files`.
  - `write_file`: Create websites/code.
  - `run_terminal_command`: Execute git/system commands.

## Installation

1. **Clone the Repository**
2. **Set Up Virtual Environment**
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Environment Configuration**
   Create a `.env` file with `OPENROUTER_API_KEY`.

## Usage

Run the main script:
```bash
python main.py
```
Or run the built EXE in `dist/`.

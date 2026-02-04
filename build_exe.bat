@echo off
echo Building Gemini Robot Pro...
pyinstaller --onefile --name "GeminiRobot" --add-data ".env;." main.py
echo Build Complete! Look in the 'dist' folder.
pause

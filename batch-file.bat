@echo off
REM Disable command echoing for cleaner output
REM Check if Python is installed
REM In my computer's case if I use "python" when running python grom command prompt I get an error.
REM After a bit of research on interned I discovered I should use "py" instead of "python".
where py >nul 2>nul
if %ERRORLEVEL% neq 0 (
    REM Display error if Python is not found
    echo Error: Python is not installed. Please install Python and try again.
    pause
    exit /b 1
)
REM Run the Python program (main.py)
py main.py
if %ERRORLEVEL% neq 0 (
    REM Display error if the program fails
    echo Error: Program failed to run. Check main.py or input CSV file.
    pause
    exit /b 1
)
REM Confirm successful execution
echo Program completed successfully. Check output.csv for results.
pause
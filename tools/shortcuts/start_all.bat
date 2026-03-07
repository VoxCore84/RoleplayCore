@echo off
setlocal
set "RUNTIME=C:\Users\atayl\VoxCore\out\build\x64-RelWithDebInfo\bin\RelWithDebInfo"
set "MYSQL_DIR=%RUNTIME%\UniServerZ\core\mysql"
set "ARCTIUM=C:\WoW\_retail_\Arctium Game Launcher.exe"

echo ============================================
echo   VoxCore — Starting All Servers
echo ============================================
echo.

:: 1. Start MySQL (UniServerZ)
echo [1/4] Starting MySQL (UniServerZ 9.5.0)...
netstat -ano | findstr ":3306 " | findstr "LISTENING" >nul 2>&1
if %ERRORLEVEL%==0 (
    echo        MySQL already running on port 3306.
) else (
    start "UniServerZ MySQL" "%MYSQL_DIR%\bin\mysqld_z.exe" ^
        "--defaults-file=%MYSQL_DIR%\my.ini" ^
        "--basedir=%MYSQL_DIR%" ^
        "--datadir=%MYSQL_DIR%\data" ^
        --port=3306 ^
        --console
    timeout /t 5 /nobreak >nul
    netstat -ano | findstr ":3306 " | findstr "LISTENING" >nul 2>&1
    if %ERRORLEVEL%==0 (
        echo        UniServerZ MySQL started.
    ) else (
        echo        WARNING: MySQL failed to start on port 3306.
        pause
        exit /b 1
    )
)
echo.

:: 2. Start bnetserver
echo [2/4] Starting bnetserver...
start "bnetserver" /D "%RUNTIME%" "%RUNTIME%\bnetserver.exe"
timeout /t 3 /nobreak >nul
echo        bnetserver launched.
echo.

:: 3. Start worldserver
echo [3/4] Starting worldserver...
start "worldserver" /D "%RUNTIME%" "%RUNTIME%\worldserver.exe"
echo        worldserver launched.
echo.

:: 4. Start Arctium Game Launcher
echo [4/4] Starting Arctium Game Launcher...
if exist "%ARCTIUM%" (
    start "" /D "C:\WoW\_retail_" "%ARCTIUM%"
    echo        Arctium launched.
) else (
    echo        WARNING: Arctium not found at %ARCTIUM%
)
echo.

echo ============================================
echo   All servers started. You can close this.
echo ============================================
timeout /t 5

@echo off
setlocal enabledelayedexpansion

:: MySQL Optimize — finds and defragments all tables with >4MB wasted space
:: Run after large imports, bulk deletes, or data audits

set "MYSQL=C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
set "USER=root"
set "PASS=admin"
set "THRESHOLD_MB=4"
set "TMPFILE=%~dp0_optimize_tmp.txt"

echo.
echo ============================================
echo   MySQL Table Optimizer
echo ============================================
echo   Threshold: %THRESHOLD_MB% MB free space
echo.

"%MYSQL%" -u %USER% -p%PASS% --batch --skip-column-names -e "SELECT CONCAT(t.TABLE_SCHEMA, '.', t.TABLE_NAME), ROUND(s.FILE_SIZE/1024/1024,1), ROUND(t.DATA_FREE/1024/1024,1) FROM information_schema.TABLES t JOIN information_schema.INNODB_TABLESPACES s ON s.NAME = CONCAT(t.TABLE_SCHEMA, '/', t.TABLE_NAME) WHERE t.TABLE_SCHEMA IN ('world','hotfixes','characters','auth','roleplay') AND t.ENGINE = 'InnoDB' AND t.DATA_FREE > %THRESHOLD_MB% * 1024 * 1024 ORDER BY t.DATA_FREE DESC;" 2>nul > "%TMPFILE%"

set "COUNT=0"
for /f "usebackq tokens=*" %%a in ("%TMPFILE%") do set /a COUNT+=1

if %COUNT%==0 (
    echo   No fragmented tables found. Everything is clean!
    echo.
    goto :done
)

echo   Found %COUNT% fragmented table(s):
echo   ------------------------------------------
for /f "usebackq tokens=1,2,3" %%a in ("%TMPFILE%") do (
    echo     %%a    file: %%b MB    wasted: %%c MB
)
echo.

set "N=0"
for /f "usebackq tokens=1" %%a in ("%TMPFILE%") do (
    set /a N+=1
    echo   [!N!/%COUNT%] OPTIMIZE TABLE %%a ...
    "%MYSQL%" -u %USER% -p%PASS% -e "OPTIMIZE TABLE %%a;" 2>nul | findstr /i "status"
)

echo.
echo   Done! %COUNT% table(s) optimized.
echo.

:done
if exist "%TMPFILE%" del "%TMPFILE%"
endlocal
pause

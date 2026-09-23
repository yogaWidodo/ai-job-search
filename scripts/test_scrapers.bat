@echo off
REM Quick smoke test for AI Job Search scraper CLIs
echo ========================================================
echo Testing AI Job Search Scraper CLIs
echo ========================================================

echo.
echo [1/2] Testing freehire-search...
cd /d "%~dp0\..\.agents\skills\freehire-search\cli"
call bun run src/cli.ts search -q "Backend Engineer Java" --limit 3 --format table
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] freehire-search failed.
) else (
    echo [OK] freehire-search executed successfully.
)

echo.
echo [2/2] Testing linkedin-search...
cd /d "%~dp0\..\.agents\skills\linkedin-search\cli"
call bun run src/cli.ts --help
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] linkedin-search failed.
) else (
    echo [OK] linkedin-search executed successfully.
)

echo.
echo All scraper CLI checks completed.
cd /d "%~dp0\.."

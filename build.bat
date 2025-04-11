@echo off
echo 📦 Building Blitz Bot EXE...


REM Build executable using PyInstaller
pyinstaller --noconfirm --clean ^
 --onefile ^
 --name "BlitzBot" ^
 --add-data "assets;assets" ^
 --add-data "tiles;tiles" ^
 --add-data "tesseract;tesseract" ^
 --hidden-import "pytesseract" ^
 main.py

echo ✅ Build complete! Check dist/BlitzBot.exe
pause

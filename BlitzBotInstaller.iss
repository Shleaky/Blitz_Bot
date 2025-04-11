; BlitzBotInstaller.iss
[Setup]
AppName=BlitzBot
AppVersion=1.0
DefaultDirName={autopf}\BlitzBot
DefaultGroupName=BlitzBot
UninstallDisplayIcon={app}\BlitzBot.exe
Compression=lzma
SolidCompression=yes
OutputDir=dist-installer
OutputBaseFilename=BlitzBotInstaller
DisableWelcomePage=no

[Files]
Source: "dist\BlitzBot.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\\*"; DestDir: "{app}\\assets"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "tiles\\*"; DestDir: "{app}\\tiles"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "tesseract\\*"; DestDir: "{app}\\tesseract"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\\BlitzBot"; Filename: "{app}\\BlitzBot.exe"
Name: "{userdesktop}\\BlitzBot"; Filename: "{app}\\BlitzBot.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional icons:"

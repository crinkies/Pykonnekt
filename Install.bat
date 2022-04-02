::License:MIT
::Author:github.com/crinkies
@echo off
mode 80,10
title Pykonnekt installer
echo Starting...
timeout 3 >nul
if not exist "%userprofile%\Documents\Pykonnekt\" (
mkdir %userprofile%\Documents\Pykonnekt\
) else (
cls
echo Folder already exists. Exiting...
timeout 3 >nul
exit
)
echo \Documents\Pykonnekt folder successfully created.
copy "Pykonnekt.pyw" "%userprofile%\Documents\Pykonnekt\"
copy "icon.ico" "%userprofile%\Documents\Pykonnekt\"
echo Python %userprofile%\Documents\Pykonnekt\Pykonnekt.pyw> %userprofile%\Documents\Pykonnekt\Start.bat
echo WScript.CreateObject("WScript.Shell").Run "%userprofile%\Documents\Pykonnekt\Start.bat", 0, True > %userprofile%\Documents\Pykonnekt\Run.vbs
echo Successfully created files in Pykonnekt folder.
echo Set shortcut = WScript.CreateObject("WScript.Shell") > Temp.vbs
echo sLinkFile = "%userprofile%\Start Menu\Programs\Startup\Pykonnekt.lnk" >> Temp.vbs
echo Set oLink = shortcut.CreateShortcut(sLinkFile) >> Temp.vbs
echo oLink.TargetPath = "%userprofile%\Documents\Pykonnekt\Run.vbs" >> Temp.vbs
echo oLink.Save >> Temp.vbs
cscript Temp.vbs
del Temp.vbs
echo Cleaning up...
echo Shortcut created in startup folder.
echo Validating files...
timeout 3 >nul
if exist %userprofile%\Documents\Pykonnekt\Pykonnekt.pyw (
        echo Pykonnekt.pyw --- OK
    ) else (
        echo Pykonnekt.pyw missing. Check install.
	timeout 3 >nul
	exit
    )
if exist %userprofile%\Documents\Pykonnekt\Start.bat (
        echo Start.bat   --- OK
    ) else (
        echo Start.bat missing. Check install.
	timeout 3 >nul
	exit
    )
if exist %userprofile%\Documents\Pykonnekt\Run.vbs (
        echo Run.vbs    --- OK
    ) else (
        echo Run.vbs missing. Check install.
	timeout 3 >nul
	exit
    )
timeout 3 >nul
echo Successfully configured to run on startup.
cls
echo Launch now? (y/n)
set /p Input=yes or no?
If /I "%Input%"=="y" goto yes
goto no
:yes
cd %userprofile%\Start Menu\Programs\Startup\
start .
start Pykonnekt.lnk
cls
timeout 3 >nul
cd %userprofile%\Documents\Pykonnekt\
Run.vbs
echo Done.
timeout 3 >nul
exit
:no
echo Launch Pykonnekt from your /Documents/Pykonnekt/ folder
echo Exiting...
timeout 3 >nul
exit

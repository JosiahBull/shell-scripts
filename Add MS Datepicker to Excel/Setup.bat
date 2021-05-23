@echo off
REM AUTHOR: JOSIAH BULL, DATE 19/05/2021
REM This file will register the Microsoft Date and Time Picker Control 6.0 (SP6)
REM It would copy the file "MSCOMCT2.OCX" to the system folder, if not exist, 
REM and register it in the registry.

REM Check this script is an administrator.
net session >nul 2>&1
if not %errorLevel% == 0 (
	echo This script requires administrator privileges. Please rerun as administrator to continue.
	goto :end	
)
 
REM Check if the file exists, if it doesn't then copy it, else ask if they want to attempt registration.
if exist %systemroot%\SysWOW64\mscomct2.ocx (
	:choice
	set /P c=File already installed on this system, skipping installation. If it's not showing up in excel, would you like to: 1. Close Prompt 2. Copy and Register 3. Register [1/2/3]?
	if /I "%c%" EQU "1" goto :end
	if /I "%c%" EQU "2" goto :copy
	if /I "%c%" EQU "3" goto :register
	goto :choice

)

:copy
echo Copying file to destination.
copy /B mscomct2.ocx /B %systemroot%\SysWOW64\mscomct2.ocx /Y

REM Regeister the file in the registry.

:register
echo Registering file.
%systemroot%\SysWOW64\regsvr32.exe mscomct2.ocx

:complete
echo Installation complete, don't forget to restart excel!

:end
echo Have a great day!

pause                


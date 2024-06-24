@echo off

:start
@REM cd C:\Users\johnb\Python_projects\Django\Sample\Backend

set mypath=%cd%
@echo %mypath%
cd %mypath%

call environment\Scripts\activate.bat
python manage.py send_sms_reminders

pause
exit
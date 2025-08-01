@echo off
echo Starting Intern Dashboard Server...
echo.
echo Access the application at:
echo - Main page: http://127.0.0.1:8000/
echo - Dashboard: http://127.0.0.1:8000/dashboard/
echo - API: http://127.0.0.1:8000/api/dashboard/
echo.
echo Press Ctrl+C to stop the server
echo.
python manage.py runserver
pause 
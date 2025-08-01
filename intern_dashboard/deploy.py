#!/usr/bin/env python3
"""
Deployment Helper Script for Intern Dashboard
This script helps prepare your Django app for deployment.
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return None

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'manage.py',
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        '.gitignore',
        'intern_dashboard_project/settings.py',
        'dashboard/views.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ All required files found")
    return True

def collect_static():
    """Collect static files"""
    return run_command("python manage.py collectstatic --noinput", "Collecting static files")

def run_migrations():
    """Run database migrations"""
    return run_command("python manage.py migrate", "Running database migrations")

def check_deployment_readiness():
    """Check if the app is ready for deployment"""
    print("🔍 Checking deployment readiness...")
    
    # Check required files
    if not check_requirements():
        return False
    
    # Check if requirements.txt has all dependencies
    with open('requirements.txt', 'r') as f:
        requirements = f.read()
        if 'gunicorn' not in requirements:
            print("⚠️  Warning: gunicorn not in requirements.txt")
        if 'whitenoise' not in requirements:
            print("⚠️  Warning: whitenoise not in requirements.txt")
    
    # Check settings.py for production settings
    with open('intern_dashboard_project/settings.py', 'r') as f:
        settings = f.read()
        if 'ALLOWED_HOSTS' not in settings:
            print("⚠️  Warning: ALLOWED_HOSTS not configured")
        if 'STATIC_ROOT' not in settings:
            print("⚠️  Warning: STATIC_ROOT not configured")
    
    print("✅ Deployment readiness check completed")
    return True

def generate_secret_key():
    """Generate a new Django secret key"""
    from django.core.management.utils import get_random_secret_key
    secret_key = get_random_secret_key()
    print(f"🔑 Generated new SECRET_KEY: {secret_key}")
    return secret_key

def main():
    """Main deployment helper function"""
    print("🚀 Intern Dashboard Deployment Helper")
    print("=" * 50)
    
    # Check deployment readiness
    if not check_deployment_readiness():
        print("❌ App is not ready for deployment. Please fix the issues above.")
        return
    
    # Generate secret key
    secret_key = generate_secret_key()
    
    # Run migrations
    run_migrations()
    
    # Collect static files
    collect_static()
    
    print("\n🎉 Deployment preparation completed!")
    print("\n📋 Next steps:")
    print("1. Create a GitHub repository")
    print("2. Push your code to GitHub")
    print("3. Choose a hosting platform:")
    print("   - Railway (recommended): https://railway.app")
    print("   - Render: https://render.com")
    print("   - Heroku: https://heroku.com")
    print("   - Cyclic: https://cyclic.sh")
    print("\n🔑 Environment variables to set:")
    print(f"SECRET_KEY={secret_key}")
    print("DEBUG=False")
    
    print("\n📖 See DEPLOYMENT.md for detailed instructions")

if __name__ == "__main__":
    main() 
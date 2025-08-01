import requests
import time

def test_server():
    """Test if the Django server is running"""
    try:
        # Wait a moment for server to start
        time.sleep(2)
        
        # Test the main page
        response = requests.get('http://127.0.0.1:8000/', timeout=5)
        print(f"Main page status: {response.status_code}")
        
        # Test the API endpoint
        response = requests.get('http://127.0.0.1:8000/api/dashboard/', timeout=5)
        print(f"API endpoint status: {response.status_code}")
        if response.status_code == 200:
            print("API Response:", response.json())
        
        print("✅ Server is running successfully!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running or not accessible")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_server() 
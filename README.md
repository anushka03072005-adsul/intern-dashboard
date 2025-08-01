# Intern Dashboard

A simple intern dashboard built with Django and Django REST Framework, featuring a modern UI for tracking donations, referral codes, and rewards.

## Features

- **Modern Login/Signup Page**: Beautiful UI with form validation
- **Dashboard Overview**: Display intern information and statistics
- **Referral Code System**: Unique referral codes for each intern
- **Donation Tracking**: Track total donations raised
- **Rewards System**: Unlockable badges and achievements
- **REST API**: Backend API endpoints for data retrieval
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Backend**: Django 5.1.7, Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default)
- **Additional**: django-cors-headers for API access

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Download the Project

Navigate to your desired directory and extract the project files.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Start the Development Server

```bash
python manage.py runserver
```

### Step 5: Access the Application

Open your browser and navigate to:
- **Main Application**: http://127.0.0.1:8000/
- **Dashboard**: http://127.0.0.1:8000/dashboard/
- **API Endpoints**: http://127.0.0.1:8000/api/

## API Endpoints

### Authentication
- `GET /api/login/` - Dummy login endpoint
- `POST /api/signup/` - Dummy signup endpoint

### Dashboard Data
- `GET /api/dashboard/` - Get intern dashboard data

### Sample API Response

```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "referral_code": "johndoe2025",
    "total_donations": 1250.00,
    "rewards": [
        {
            "id": 1,
            "name": "Bronze Badge",
            "description": "Complete your first donation campaign",
            "points_required": 100,
            "is_unlocked": true
        }
    ]
}
```

## Project Structure

```
intern_dashboard/
├── intern_dashboard_project/    # Main Django project
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI configuration
├── dashboard/                   # Main app
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── serializers.py          # API serializers
│   ├── urls.py                 # App URL configuration
│   └── templates/
│       └── dashboard/
│           ├── login.html      # Login/signup page
│           └── dashboard.html  # Main dashboard
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Features in Detail

### 1. Login/Signup Page
- Toggle between login and signup forms
- Form validation and error handling
- Success messages and redirects
- Modern gradient design

### 2. Dashboard
- **Welcome Section**: Personalized greeting
- **Statistics Cards**: 
  - Total donations raised
  - Rewards unlocked
  - Campaigns completed
- **Referral Code Section**: 
  - Display unique referral code
  - Click to copy functionality
- **Rewards Section**: 
  - Visual reward cards
  - Locked/unlocked status
  - Progress tracking

### 3. API Features
- RESTful API design
- JSON responses
- CORS enabled for cross-origin requests
- Dummy data for demonstration

## Customization

### Changing Dummy Data

To modify the dummy data, edit the `api_dashboard` function in `dashboard/views.py`:

```python
dummy_intern_data = {
    'name': 'Your Name',
    'referral_code': 'yourname2025',
    'total_donations': 2000.00,
    # ... modify other fields
}
```

### Adding New Rewards

Add new rewards to the rewards array in the API response:

```python
{
    'id': 6,
    'name': 'New Badge',
    'description': 'Description of the new badge',
    'points_required': 3000,
    'is_unlocked': False
}
```

### Styling Customization

The CSS is embedded in the HTML templates. You can modify:
- Color scheme in CSS variables
- Layout and spacing
- Animations and transitions
- Responsive breakpoints

## Testing with Postman

1. **Login Test**:
   - Method: GET
   - URL: `http://127.0.0.1:8000/api/login/`

2. **Signup Test**:
   - Method: POST
   - URL: `http://127.0.0.1:8000/api/signup/`
   - Body: JSON (optional for dummy endpoint)

3. **Dashboard Data Test**:
   - Method: GET
   - URL: `http://127.0.0.1:8000/api/dashboard/`

## Future Enhancements

- User authentication with Django's built-in auth system
- Database integration for real data storage
- Admin panel for managing interns and rewards
- Real-time updates with WebSockets
- Email notifications for achievements
- Social sharing features
- Analytics and reporting

## Troubleshooting

### Common Issues

1. **Port Already in Use**:
   ```bash
   python manage.py runserver 8001
   ```

2. **Migration Errors**:
   ```bash
   python manage.py makemigrations --empty dashboard
   python manage.py migrate
   ```

3. **Static Files Not Loading**:
   - Ensure `DEBUG = True` in settings.py
   - Check that templates are in the correct directory

### Support

For issues or questions, check the Django documentation or create an issue in the project repository.

## 🚀 Deployment

This application is ready for deployment to various hosting platforms. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

### Quick Deploy Options:

1. **Railway** (Recommended - Free & Easy)
   - Go to [railway.app](https://railway.app)
   - Connect your GitHub repository
   - Automatic deployment

2. **Render** (Free Tier)
   - Go to [render.com](https://render.com)
   - Create new Web Service
   - Connect your repository

3. **Heroku** (Paid)
   - Install Heroku CLI
   - `heroku create your-app-name`
   - `git push heroku main`

4. **Cyclic** (Free Tier)
   - Go to [cyclic.sh](https://cyclic.sh)
   - Link your repository
   - Automatic deployment

### Pre-deployment Checklist:

```bash
# Run the deployment helper
python deploy.py

# Or manually:
python manage.py migrate
python manage.py collectstatic --noinput
```

## License

This project is created for educational and demonstration purposes. 
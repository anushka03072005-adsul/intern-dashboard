from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Intern, Reward
from .serializers import InternSerializer, RewardSerializer
import json

def login_page(request):
    """Render login page"""
    return render(request, 'dashboard/login.html')

@api_view(['POST'])
def signup(request):
    """Dummy signup endpoint"""
    return Response({
        'message': 'Signup successful',
        'user_id': 1
    })

def dashboard_data(request):
    """Render dashboard page"""
    return render(request, 'dashboard/dashboard.html')

@api_view(['GET'])
def api_dashboard(request):
    """API endpoint for dashboard data"""
    # For demo purposes, we'll return dummy data
    # In a real app, you'd get the user from the session/token
    
    dummy_intern_data = {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'referral_code': 'johndoe2025',
        'total_donations': 1250.00,
        'rewards': [
            {
                'id': 1,
                'name': 'Bronze Badge',
                'description': 'Complete your first donation campaign',
                'points_required': 100,
                'is_unlocked': True
            },
            {
                'id': 2,
                'name': 'Silver Badge',
                'description': 'Raise $500 in donations',
                'points_required': 500,
                'is_unlocked': True
            },
            {
                'id': 3,
                'name': 'Gold Badge',
                'description': 'Raise $1000 in donations',
                'points_required': 1000,
                'is_unlocked': True
            },
            {
                'id': 4,
                'name': 'Platinum Badge',
                'description': 'Raise $2000 in donations',
                'points_required': 2000,
                'is_unlocked': False
            },
            {
                'id': 5,
                'name': 'Diamond Badge',
                'description': 'Raise $5000 in donations',
                'points_required': 5000,
                'is_unlocked': False
            }
        ]
    }
    
    return Response(dummy_intern_data)

@api_view(['GET'])
def api_login(request):
    """API endpoint for login"""
    return login_page(request)

@api_view(['POST'])
def api_signup(request):
    """API endpoint for signup"""
    return signup(request)

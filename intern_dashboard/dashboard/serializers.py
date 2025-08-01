from rest_framework import serializers
from .models import Intern, Reward

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['id', 'name', 'description', 'points_required', 'is_unlocked']

class InternSerializer(serializers.ModelSerializer):
    rewards = RewardSerializer(many=True, read_only=True)
    
    class Meta:
        model = Intern
        fields = ['id', 'name', 'email', 'referral_code', 'total_donations', 'rewards'] 
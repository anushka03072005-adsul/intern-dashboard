from django.db import models

# Create your models here.

class Intern(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    referral_code = models.CharField(max_length=50, unique=True)
    total_donations = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.referral_code}"

class Reward(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    points_required = models.IntegerField()
    is_unlocked = models.BooleanField(default=False)
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE, related_name='rewards')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.points_required} points"

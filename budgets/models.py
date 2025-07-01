from django.db import models
from users.models import CustomUser

class Budget(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=10, choices=[('Monthly', 'Monthly'), ('Weekly', 'Weekly')])
    created_at = models.DateTimeField(auto_now_add=True)

class SavingGoal(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()

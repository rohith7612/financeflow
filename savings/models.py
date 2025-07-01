from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    target_date = models.DateField()

    def progress_percentage(self):
        return (self.saved_amount / self.target_amount) * 100 if self.target_amount else 0

    def __str__(self):
        return f"{self.title} - {self.user.username}"

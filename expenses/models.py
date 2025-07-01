from django.db import models
from users.models import CustomUser

CATEGORY_CHOICES = [
    ('Food', 'Food'), ('Transport', 'Transport'), ('Bills', 'Bills'),
    ('Entertainment', 'Entertainment'), ('Shopping', 'Shopping'), 
    ('Health', 'Health'), ('Other', 'Other'),
]

class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    date = models.DateField()
    note = models.TextField(blank=True, null=True)
    receipt = models.ImageField(upload_to='receipts/', blank=True, null=True)
    is_recurring = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.amount}"

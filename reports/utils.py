# reports/utils.py
from expenses.models import Expense
from django.db.models import Sum
from datetime import date, timedelta

def get_daily_report(user):
    today = date.today()
    return Expense.objects.filter(user=user, date=today).aggregate(total=Sum('amount'))

def get_weekly_report(user):
    today = date.today()
    week_ago = today - timedelta(days=7)
    return Expense.objects.filter(user=user, date__range=[week_ago, today]).aggregate(total=Sum('amount'))

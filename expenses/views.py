from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('list_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add.html', {'form': form})

@login_required
def list_expenses(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'expenses/list.html', {'expenses': expenses})

@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('list_expenses')
    else:
        form = ExpenseForm(instance=expense)
    
    return render(request, 'expenses/edit.html', {'form': form, 'expense': expense})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    
    if request.method == 'POST':
        expense.delete()
        return redirect('list_expenses')
    
    return render(request, 'expenses/delete.html', {'expense': expense})

from django.db.models import Sum
from datetime import date, timedelta
from django.utils.timezone import now

@login_required
def dashboard(request):
    today = date.today()
    month_ago = today.replace(day=1)

    user = request.user

    # Expense aggregations
    monthly_total = Expense.objects.filter(user=user).aggregate(total=Sum('amount'))['total'] or 0

    # Category-wise breakdown for all expenses
    category_data = Expense.objects.filter(user=user).values('category').annotate(total=Sum('amount')).order_by('-total')
    
    # Calculate average per category
    category_count = category_data.count()
    avg_per_category = 0
    if category_count > 0:
        avg_per_category = round(monthly_total / category_count, 2)
    
    # Daily expense data for the past week
    daily_expense_data = []
    for i in range(7):
        day = today - timedelta(days=6-i)
        daily_amount = Expense.objects.filter(user=user, date=day).aggregate(total=Sum('amount'))['total'] or 0
        daily_expense_data.append({'day': day.strftime('%a'), 'total': daily_amount})
    
    return render(request, 'expenses/dashboard.html', {
        'monthly_total': monthly_total,
        'category_data': category_data,
        'daily_expense_data': daily_expense_data,
        'avg_per_category': avg_per_category,
    })

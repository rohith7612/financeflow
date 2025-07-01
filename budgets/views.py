from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Budget
from .forms import BudgetForm
from expenses.models import Expense
from datetime import date, timedelta
from django.db.models import Sum
from decimal import Decimal

@login_required
def create_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('view_budgets')
    else:
        form = BudgetForm()
    return render(request, 'budgets/add.html', {'form': form})


@login_required
def view_budgets(request):
    budgets = Budget.objects.filter(user=request.user)
    alerts = []
    total_spent_all = Decimal('0.00')

    for budget in budgets:
        # Determine the start date based on the budget period
        if budget.period == 'Monthly':
            start_date = date.today().replace(day=1)
        elif budget.period == 'Weekly':
            start_date = date.today() - timedelta(days=7)
        else:
            start_date = None

        # Calculate total spent for this category and user in the given period
        spent = Expense.objects.filter(
            user=request.user,
            category=budget.category,
            date__gte=start_date
        ).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')

        # Save for total calculation
        total_spent_all += spent

        # Warnings based on limits
        if spent >= budget.limit:
            alerts.append(f"⚠️ You have exceeded your {budget.period.lower()} budget for {budget.category}")
        elif spent >= Decimal('0.8') * budget.limit:
            alerts.append(f"⚠️ You're close to your {budget.period.lower()} budget for {budget.category}")

        # Attach data for template use
        budget.spent = spent
        try:
            budget.percentage = (spent / budget.limit) * 100
        except ZeroDivisionError:
            budget.percentage = 0
            
        # Set status based on percentage
        if spent >= budget.limit:
            budget.status = 'over'
        elif spent >= Decimal('0.7') * budget.limit:
            budget.status = 'warning'
        elif spent >= Decimal('0.5') * budget.limit:
            budget.status = 'halfway'
        else:
            budget.status = 'good'

    return render(request, 'budgets/list.html', {
        'budgets': budgets,
        'alerts': alerts,
        'total_spent': total_spent_all
    })

@login_required
def edit_budget(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id, user=request.user)
    
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('view_budgets')
    else:
        form = BudgetForm(instance=budget)
    
    return render(request, 'budgets/edit.html', {'form': form, 'budget': budget})

@login_required
def delete_budget(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id, user=request.user)
    
    if request.method == 'POST':
        budget.delete()
        return redirect('view_budgets')
    
    return render(request, 'budgets/delete.html', {'budget': budget})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SavingsGoalForm
from .models import SavingsGoal
from django.shortcuts import get_object_or_404

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('view_goals')
    else:
        form = SavingsGoalForm()
    return render(request, 'savings/add.html', {'form': form})

@login_required
def view_goals(request):
    goals = SavingsGoal.objects.filter(user=request.user)
    return render(request, 'savings/list.html', {'goals': goals})

@login_required
def update_goal(request, goal_id):
    goal = get_object_or_404(SavingsGoal, id=goal_id, user=request.user)

    if request.method == 'POST':
        form = SavingsGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('view_goals')
    else:
        form = SavingsGoalForm(instance=goal)

    return render(request, 'savings/update.html', {'form': form, 'goal': goal})

@login_required
def delete_goal(request, goal_id):
    goal = get_object_or_404(SavingsGoal, id=goal_id, user=request.user)
    
    if request.method == 'POST':
        goal.delete()
        return redirect('view_goals')
    
    return render(request, 'savings/delete.html', {'goal': goal})
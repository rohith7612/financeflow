from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.create_budget, name='add_budget'),
    path('list/', views.view_budgets, name='view_budgets'),
    path('edit/<int:budget_id>/', views.edit_budget, name='edit_budget'),
    path('delete/<int:budget_id>/', views.delete_budget, name='delete_budget'),
]

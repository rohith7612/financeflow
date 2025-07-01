from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_goal, name='add_goal'),
    path('list/', views.view_goals, name='view_goals'),
    path('update/<int:goal_id>/', views.update_goal, name='update_goal'),
    path('delete/<int:goal_id>/', views.delete_goal, name='delete_goal'),
]

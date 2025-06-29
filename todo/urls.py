from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
    path('update/<int:task_id>/', views.update_task, name='update'),
    path('toggle/<int:task_id>/', views.toggle_complete, name='toggle'),
]

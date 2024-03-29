
from django.urls import path
from .views import login, register_view, dashboard, add_task_view

urlpatterns = [
    path('',login, name="login page"),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_task/', add_task_view, name='add_task_view'),


]

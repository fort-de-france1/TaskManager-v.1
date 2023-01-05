from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path('done/', views.done, name="index" ),
    path('', views.all_tasks, name="tasks" ),
    path('add/', views.add, name="add" ),
    path('add_task/', views.add_task, name="add_task" ),
    path('<int:pk>/change/', views.change_status, name="change_status" ),
]

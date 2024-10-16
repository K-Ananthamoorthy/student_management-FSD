from django.urls import path
from . import views
from .views import create_superuser

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/new/', views.student_create, name='student_create'),
    path('create-superuser/', create_superuser),
]

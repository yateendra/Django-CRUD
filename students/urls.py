from django.urls import path
from .views import index, add, edit, delete

app_name = 'students'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('edit/<int:student_id>/', edit, name='edit'),
    path('delete/<int:student_id>/', delete, name='delete'),
]

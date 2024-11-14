from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_records, name='view_records'),
    path('edit/', views.edit_record, name='edit_record'),
    path('history/', views.view_history, name='view_history'),
    path('add/', views.add_record, name='add_record'),
]

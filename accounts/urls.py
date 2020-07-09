from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('consumer/', views.consumer_registration, name='consumer_registration'),
    path('pharmacy/', views.pharmacy_registration, name='pharmacy_registration'),
    path('pharmacy/add/', views.add_drug, name='add_drug'),
    path('pharmacy/drug/<int:drug_id>/edit/', views.edit_drug, name='edit_drug'),
    path('pharmacy/drug/<int:drug_id>/delete/', views.delete_drug, name='delete_drug'),
    path('pharmacy/ots/', views.pharmacy_setup, name='pharmacy_setup'),
    path('login/', views.authLogin, name='login'),
]
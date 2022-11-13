from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('get_patients/', views.get_patients, name='get_patients'),
    path('set_donation_status/', views.set_donation_status, name='set_donation_status'),
    path('set_patient_status/', views.set_patient_status, name='set_patient_status'),
    path('agree_to_donate/', views.agree_to_donate, name='agree_to_donate')
]

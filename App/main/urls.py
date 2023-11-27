from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('main/delete_appointment/<int:appointment_id>', views.delete_appointment, name = 'delete_appointment'),
    path('main/appointments/', views.appointments, name = 'appointments')
]

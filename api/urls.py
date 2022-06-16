from django.urls import path
from . import views


urlpatterns = [
    path('symptoms/', views.getSymptoms, name="symptoms"),
    path('add/', views.addSymptoms)
]
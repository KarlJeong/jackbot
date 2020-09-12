from django.urls import path
from . import views

app_name = 'jackbot_simulator'
urlpatterns = [
    path('', views.SimulatorView.as_view()),
]

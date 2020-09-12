from django.urls import path
from .views import mainView

app_name = 'jackbot_collector'
urlpatterns = [
    path('', mainView.CollectorView.as_view()),
]

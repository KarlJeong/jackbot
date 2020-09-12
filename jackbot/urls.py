from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('collector/', include('jackbot_collector.urls'), name='jackbot_collector'),
    path('simulator/', include('jackbot_simulator.urls'), name='jackbot_simulator'),
]

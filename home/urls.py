from django.urls import path
from home.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('site-under-maintenance', SiteUnderMaintenanceView.as_view(), name='site_under_maintenance'),
]



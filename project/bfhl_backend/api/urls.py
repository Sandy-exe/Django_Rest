from django.urls import path
from .views import BFHLAPIView, index

# bfhl_app/urls.py (update this file)
urlpatterns = [
    path('', index, name='index'),
    path('bfhl/', BFHLAPIView.as_view(), name='bfhl_api'),
]

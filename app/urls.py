
from django.urls import path
from .views import PrimeGenerateView

urlpatterns = [
    path('prime/',PrimeGenerateView.as_view())
]
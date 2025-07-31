from django.urls import path
from .views import CreateCheckoutSession


urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSession.as_view()),
]
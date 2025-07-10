from django.urls import path
from .views import RegisterView, MyTokenObtianPairView

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtianPairView.as_view(), name='token_obtain_pair'),

]
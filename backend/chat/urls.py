from django.urls import path
from .views import SignUpView, LoginView

urlpatterns = [
    path('users/signup/', SignUpView.as_view(), name='signup'),
    path('users/login/', LoginView.as_view(), name='login'),
]


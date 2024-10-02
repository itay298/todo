from django.urls import path
from .views import UserLoginView, UserSignupView, UserLogoutView

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/signup/', UserSignupView.as_view(), name='signup'),
    path('accounts/logout/', UserLogoutView.as_view(), name='logout'),
]

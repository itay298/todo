from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

# PasswordChangeView, PasswordResetView !!!!

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class UserSignupView(generic.CreateView):
    template_name = 'accounts/signup.html'
    model = get_user_model()
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    
class UserLogoutView(LogoutView):
    success_url_allowed_hosts = reverse_lazy('todo:index')

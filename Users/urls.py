from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='Users/login.html'), name='LOGIN'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html', next_page = 'L'), name='LOGOUT'),
    path('regitser/', views.Register_User, name='REGISTER')
]
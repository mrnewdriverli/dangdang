from django.urls import path, include
from user import views
app_name = 'user'
urlpatterns = [
    path('login/',views.login, name='login'),
    path('login_logic/',views.login_logic, name='login_logic'),
    path('register/',views.register, name='register'),
    path('register_logic/',views.register_logic, name='register_logic'),
    path('get_captcha/',views.get_captcha, name='get_captcha'),
    path('check_name/',views.check_name, name='check_name'),
    path('check_password/',views.check_password, name='check_password'),
    path('register_ok/',views.register_ok, name='register_ok'),
    path('logout/',views.logout, name='logout')
]


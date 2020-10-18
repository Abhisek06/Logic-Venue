from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login', views.Login, name='login'),
    path('password_reset', views.password_reset, name='password_reset'),
    path('addition', views.addition, name='addition'),
]

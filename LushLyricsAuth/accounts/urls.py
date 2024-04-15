from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name='home'),  
    path('secure/', views.my_secure_view, name='secure'),
    path('login/', views.user_login, name='login'),  # Rename the login view
    path('register/', views.register, name='register'),
    path('authorized/', views.my_authorized_view, name='authorized'),
    path('logout/', views.logout_view, name='logout'), 
    path('password_recovery/', views.password_recovery, name='password_recovery'),
    path('password_reset_done/', views.custom_password_reset_done, name='password_reset_done'),
    # Other URL patterns
]

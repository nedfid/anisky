from django.urls import path
from user import views

urlpatterns = [
    path('all/', views.user_all, name='user_all'),
    path('<username>/', views.user_profile, name='user_profile'),
    path('<username>/settings/', views.user_settings, name='user_settings'),
]
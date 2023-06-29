from django.urls import path, include

from quiz.main_page import views

urlpatterns = (
    path('', views.home_page, name='welcome page'),
    path('login/', views.logging_page, name='login page'),
    path('register/', views.register_page, name='register page'),
    path('profile/', views.profile_page, name='profile page'),

    # extends for another app

)

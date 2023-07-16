from django.urls import path, include

from quiz.main_page import views

urlpatterns = (
    path('', views.home_page, name='welcome page'),
    path('login/', views.UserLoginView.as_view(), name='login page'),
    path('logout/', views.UserLogoutForm.as_view(), name='logout page'),
    path('register/', views.RegisterUserView.as_view(), name='register page'),
    path('profile/', include([
         path('details/<int:pk>/', views.UserProfileEditView.as_view(), name='profile details'),

    ])),
)

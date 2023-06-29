
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.main_page.urls')),
    path('', include('quiz.quiz_page.urls')),
]

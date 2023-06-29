from django.urls import path, include

from quiz.quiz_page import views

urlpatterns = (
    path('categories/', include([
        path('', views.categories_page, name='categories page'),
        path('random/', views.random_quiz, name='random quiz'),
        path('History/', views.HistoryView.as_view(), name='History'),
    ])),
    path('create-question/', views.CreateQuestionView.as_view(), name='create question'),

)

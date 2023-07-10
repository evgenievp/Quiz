from django.urls import path, include

from quiz.quiz_page import views

urlpatterns = (
    path('categories/', include([
        path('', views.CategoriesPage.as_view(), name='categories page'),
        path('random/', views.random_quiz, name='random quiz'),
        path('History/', views.HistoryView.as_view(), name='History'),
        path('Philosophy/', views.PhilosophyView.as_view(), name="Philosophy"),
        path('Literature/', views.LiteratureView.as_view(), name='Literature'),
        #path('Programming/', views.ProgrammingView.as_view(), name='Programming'),
    ])),
    path('create-question/', views.CreateQuestionView.as_view(), name='create question'),

)

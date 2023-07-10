from django.contrib import admin

from quiz.main_page.models import QuizUser
from quiz.quiz_page.models import Question, Category, Quiz


@admin.register(Question)
class QuestionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass


@admin.register(QuizUser)
class UserAdminPanel(admin.ModelAdmin):
    pass

from django.contrib import admin
from quiz.quiz_page.models import Question, Category


@admin.register(Question)
class QuestionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    pass

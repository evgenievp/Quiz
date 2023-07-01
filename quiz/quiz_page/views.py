from django.shortcuts import render
from django.urls import reverse_lazy
from quiz.quiz_page.forms import QuizForm, CreateQuestionForm
from quiz.quiz_page.models import Question, Category
from django.views import generic as views


def categories_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories/categories.html', context)


def random_quiz(request):
    five_questions = Question.objects.all()[:5]
    form = QuizForm()
    context = {
        'form': form,
        'questions': five_questions,
        'questions_count': five_questions.count(),
        'topic': 'Random',

    }
    return render(request, 'quiz_page/random_quiz.html', context)


class HistoryView(views.CreateView):
    model = Category
    template_name = 'quiz_page/history_quiz.html'
    fields = '__all__'
    success_url = reverse_lazy('categories page')
    random_five = Question.objects.filter(topic__name='History')[:5]
    extra_context = {
        'topic': "History",
        'random_five': random_five,
    }


class PhilosophyView(views.CreateView):
    model = Category
    template_name = 'quiz_page/philosophy_quiz.html'
    fields = '__all__'
    success_url = reverse_lazy('categories page')
    random_five = Question.objects.filter(topic__name='Philosophy').order_by("?")[:5]
    extra_context = {
        'topic': "Philosophy",
        'random_five': random_five,
    }


class CreateQuestionView(views.CreateView):
    model = Question
    template_name = 'questions/add_question.html'
    success_url = reverse_lazy('categories page')
    form_class = CreateQuestionForm




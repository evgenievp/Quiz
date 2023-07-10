from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from quiz.quiz_page.forms import QuizForm, CreateQuestionForm
from quiz.quiz_page.models import Question, Category
from django.views import generic as views


class CategoriesPage(LoginRequiredMixin, views.ListView):
    template_name = 'categories/categories.html'
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'


@login_required
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



class HistoryView(LoginRequiredMixin, views.View):
    model = Category
    template_name = 'quiz_page/history_quiz.html'
    fields = '__all__'
    success_url = reverse_lazy('categories page')
    random_five = Question.objects.filter(topic__name='History')[:5]
    extra_context = {
        'topic': "History",
        'random_five': random_five,
    }


class PhilosophyView(LoginRequiredMixin, views.View):
    model = Category
    template_name = 'quiz_page/philosophy_quiz.html'
    fields = '__all__'
    success_url = reverse_lazy('categories page')
    random_five = Question.objects.filter(topic__name='Philosophy').order_by("?")[:5]
    extra_context = {
        'topic': "Philosophy",
        'random_five': random_five,
    }


class LiteratureView(LoginRequiredMixin, views.CreateView):
    model = Category
    template_name = 'quiz_page/literature_quiz.html'
    fields = '__all__'
    success_url = reverse_lazy('categories page')
    random_five = Question.objects.filter(topic__name='Literature').order_by("?")[:5]
    extra_context = {
        'topic': "Literature",
        'random_five': random_five,
    }



class ProgrammingView(LoginRequiredMixin, views.View):
    model = Category
    template_name = 'quiz_page/programming.html'
    fields = '__all__'
    succcess_url = reverse_lazy('categories page')
    random_five = Question.objects.filter(topic__name='Programming').order_by("?")[:5]
    extra_content = {
        'topic': 'Programming',
        'random_five': random_five,
    }


class CreateQuestionView(LoginRequiredMixin, views.View):
    model = Question
    template_name = 'questions/add_question.html'
    success_url = reverse_lazy('categories page')
    form_class = CreateQuestionForm




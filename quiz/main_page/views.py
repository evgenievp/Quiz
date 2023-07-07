from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from quiz.main_page.forms import RegisterForm, LoginForm, UserProfileEditForm
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from quiz.main_page.models import QuizUser


def home_page(request):
    if request.method == "GET":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome page')
    context = {
        'form': RegisterForm(),
    }

    return render(request, 'home_page/welcome_page.html', context=context)


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'logging-page.html'
    next_page = reverse_lazy('categories page')


class UserLogoutForm(auth_views.LogoutView):
    next_page = reverse_lazy('welcome page')


class RegisterUserView(views.CreateView):
    template_name = 'register-page.html'
    model = QuizUser
    form_class = RegisterForm
    success_url = 'profile details'

    def form_valid(self, form):
        response = super().form_valid(form)
        profile_details_url = reverse_lazy('profile details', kwargs={'pk': self.object.pk})
        return redirect(profile_details_url)


class UserProfileEditView(views.UpdateView):
    model = QuizUser
    form_class = UserProfileEditForm
    template_name = 'profile-page.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk', self.object.pk})



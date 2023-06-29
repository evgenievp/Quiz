from django.shortcuts import render, redirect
from quiz.main_page.forms import RegisterForm


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


def logging_page(request):
    return render(request, 'logging-page.html')


def register_page(request):
    if request.method == "GET":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    context = {
        'form': form,
    }
    return render(request, 'register-page.html', context)


def profile_page(request):
    context = {

    }
    return render(request, 'profile-page.html', context)


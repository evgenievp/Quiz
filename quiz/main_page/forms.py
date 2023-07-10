from django import forms
from quiz.main_page.models import QuizUser
from django.contrib.auth import forms as auth_forms


class MyUserForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = QuizUser
        fields = ('username', 'email', 'password')


class LoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(widget=forms.TextInput(attrs={'autofocus': True, "placeholder": "username"}))
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Username"
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['username'].error_messages = {'required': '', 'label': None}
        self.fields['password'].error_messages = {'required': '', 'label':  None}

    class Meta:
        help_texts = {
            'username': "",
            'password': '',
        }
        label = {
            'username': '',
            'password': '',
        }


class RegisterForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'example@mail.com'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'

    class Meta(auth_forms.UserCreationForm.Meta):
        model = QuizUser
        fields = ('username', 'email')
        labels = {
            'username': '',
            'password': '',
            'email': '',
        }
        help_texts = {
            'username': None,
            'password': None,
            'email': None,
        }


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = QuizUser
        fields = '__all__'

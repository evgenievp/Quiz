from django import forms
from quiz.main_page.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['profile_image']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Example@email.com',
                }
            ),
        }

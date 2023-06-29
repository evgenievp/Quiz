from django import forms
from quiz.quiz_page.models import Question


class QuizForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class CreateQuestionForm(QuizForm):
    class Meta:
        model = Question
        fields = '__all__'
        labels = {
            'question': '',
            'option_1': '',
            'option_2': '',
            'option_3': '',
            'option_4': '',
        }
        widgets = {
            'question': forms.Textarea(
                attrs={
                    'placeholder': "Enter Your question here. (Max 300 symbols)"
                }
            ),
        }

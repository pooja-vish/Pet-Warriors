from django import forms
from PetForum.models import Member, Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'category']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(label='Your Qestion',max_length=550)

class AnswerForm(forms.Form):
    answer = forms.CharField(label='Your Answer', max_length=5000)
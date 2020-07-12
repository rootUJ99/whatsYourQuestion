from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label='', max_length=550, 
    widget=forms.TextInput(attrs={'class': "input_question"})
    )


class AnswerForm(forms.Form):
    answer = forms.CharField(label='Your Answer', max_length=5000)


class SearchQuestion(forms.Form):
    search = forms.CharField(label='search question', max_length=550)

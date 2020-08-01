from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
    )
    question = models.CharField(max_length=550)
    # tags = models
    question_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question}'


class Answer(models.Model):
    user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=5000)
    answer_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.answer}'

class Comment(models.Model):
    user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
    )
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    comment = models.CharField(max_length= 5000)
    comment_data = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.comment}'

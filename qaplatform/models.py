from django.db import models

# Create your models here.
class Question(models.Model):
  question = models.CharField(max_length=550)
  # tags = models
  question_date = models.DateTimeField('date published')
  
  def __str__(self):
    return f'{self.question}'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=5000)
    answer_date = models.DateTimeField('date published')

    def __str__(self):
      return f'{self.answer}'
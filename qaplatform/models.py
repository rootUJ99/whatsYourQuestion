from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
class Vote(models.Model):
	upvote = models.ForeignKey(get_user_model(), related_name='upvoter', null=True, blank=True, on_delete=models.CASCADE
    )
	downvote = models.ForeignKey(get_user_model(), related_name='downvoter', null=True, blank=True, on_delete=models.CASCADE
    )
	class Meta:
		unique_together=('upvote', 'downvote')

class Question(models.Model):
	user = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)
	question = models.CharField(max_length=280)
	description = models.CharField(max_length=800)
	question_date = models.DateTimeField('date published', default=timezone.now())
	vote = models.ForeignKey(Vote, on_delete=models.CASCADE, default=None, null=True)

	def __str__(self):
		return f'{self.question}'


class Answer(models.Model):
	user = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.CharField(max_length=10000)
	answer_date = models.DateTimeField('date published', default=timezone.now())
	vote = models.ForeignKey(Vote, on_delete=models.CASCADE, default=None, null=True)

	def __str__(self):
		return f'{self.answer}'

class Comment(models.Model):
	user = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	comment = models.CharField(max_length= 5000)
	comment_date = models.DateTimeField('date published', default=timezone.now())
	vote = models.ForeignKey(Vote, on_delete=models.CASCADE, default=None, null=True)
	def __str__(self):
		return f'{self.comment}'

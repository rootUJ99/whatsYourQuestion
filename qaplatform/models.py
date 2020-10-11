from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser
# Create your models here.

# class CustomUser(AbstractUser):
# 	points = models.IntegerField(
#     default=0
#   ),
# 	follower = models.TextField(default=None),
# 	following = models.TextField(default=None),

class Question(models.Model):
	user = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)
	question = models.CharField(max_length=280)
	description = models.CharField(max_length=800)
	# tags = models
	question_date = models.DateTimeField('date published')
	new_upvote = models.ForeignKey(get_user_model(), related_name='que_upvoter', on_delete=models.CASCADE, blank=True,
    null=True)
	new_downvote = models.ForeignKey(get_user_model(), related_name='que_downvoter', on_delete=models.CASCADE, blank=True,
    null=True)
	upvote = models.IntegerField(default=0)
	downvote = models.IntegerField(default=0)

	class Meta:
		unique_together = ('new_upvote', 'new_downvote')

	def __str__(self):
		return f'{self.question}'


class Answer(models.Model):
	user = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.CharField(max_length=10000)
	answer_date = models.DateTimeField('date published')
	new_upvote = models.ForeignKey(get_user_model(), related_name='ans_upvoter', on_delete=models.CASCADE, blank=True,
    null=True)
	new_downvote = models.ForeignKey(get_user_model(), related_name='ans_downvoter', on_delete=models.CASCADE, blank=True,
    null=True)
	upvote = models.IntegerField(default=0)
	downvote = models.IntegerField(default=0)

	class Meta:
		unique_together = ('new_upvote', 'new_downvote')

	def __str__(self):
		return f'{self.answer}'

class Comment(models.Model):
	user = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	comment = models.CharField(max_length= 5000)
	comment_date = models.DateTimeField('date published')
	new_upvote = models.ForeignKey(get_user_model(), related_name='comm_upvoter', on_delete=models.CASCADE, blank=True,
    null=True)
	new_downvote = models.ForeignKey(get_user_model(), related_name='comm_downvoter', on_delete=models.CASCADE, blank=True,
    null=True)
	upvote = models.IntegerField(default=0)
	downvote = models.IntegerField(default=0)

	class Meta:
		unique_together = ('new_upvote', 'new_downvote')
	def __str__(self):
		return f'{self.comment}'

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

# class Follower(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class UserFollowing(models.Model):
    profile = models.ForeignKey(Profile, related_name="followers", on_delete=models.CASCADE)
    profile_following = models.ForeignKey(Profile, related_name="following", on_delete=models.CASCADE)
    class Meta:
        unique_together = ("profile", "profile_following")


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    

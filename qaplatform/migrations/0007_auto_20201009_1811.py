# Generated by Django 3.1 on 2020-10-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qaplatform', '0006_auto_20200815_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]

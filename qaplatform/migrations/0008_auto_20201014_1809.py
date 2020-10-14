# Generated by Django 3.1 on 2020-10-14 18:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qaplatform', '0007_auto_20201014_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 14, 18, 9, 5, 6569), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 14, 18, 9, 5, 7068), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 14, 18, 9, 5, 6078), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downvote', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='downvoter', to=settings.AUTH_USER_MODEL)),
                ('upvote', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upvoter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('upvote', 'downvote')},
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='vote',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='qaplatform.vote'),
        ),
        migrations.AddField(
            model_name='comment',
            name='vote',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='qaplatform.vote'),
        ),
        migrations.AddField(
            model_name='question',
            name='vote',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='qaplatform.vote'),
        ),
    ]

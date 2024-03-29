# Generated by Django 3.1 on 2020-10-14 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qaplatform', '0006_auto_20200815_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 14, 17, 53, 56, 883464), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 14, 17, 53, 56, 884053), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 14, 17, 53, 56, 882898), verbose_name='date published'),
        ),
    ]

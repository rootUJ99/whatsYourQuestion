# Generated by Django 3.0.8 on 2020-07-27 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qaplatform', '0002_auto_20200325_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=5000)),
                ('comment_data', models.DateTimeField(verbose_name='date published')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qaplatform.Answer')),
            ],
        ),
    ]

# Generated by Django 2.2.9 on 2020-01-14 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_prompt',
            field=models.CharField(default='', max_length=200),
        ),
    ]

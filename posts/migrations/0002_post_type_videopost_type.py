# Generated by Django 4.2 on 2025-01-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('video', 'Video'), ('tutorial', 'Tutorial'), ('youtube', 'YouTube')], default='text', max_length=32),
        ),
        migrations.AddField(
            model_name='videopost',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('video', 'Video'), ('tutorial', 'Tutorial'), ('youtube', 'YouTube')], default='video', max_length=32),
        ),
    ]

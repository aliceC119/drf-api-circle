# Generated by Django 5.1.4 on 2025-01-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../https://res.cloudinary.com/dydlslgyc/image/upload/v1734949456/default_post_mgvuq6.jpg', upload_to='images/'),
        ),
    ]
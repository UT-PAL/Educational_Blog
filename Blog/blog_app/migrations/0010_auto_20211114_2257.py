# Generated by Django 3.1 on 2021-11-14 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_auto_20211114_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=models.TextField(verbose_name='What is on your mind?'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(upload_to='blog_images', verbose_name='Image'),
        ),
    ]

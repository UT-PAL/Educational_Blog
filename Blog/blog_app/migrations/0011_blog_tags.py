# Generated by Django 3.1 on 2021-11-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_auto_20211114_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.CharField(max_length=264, null=True, verbose_name='Put a tag '),
        ),
    ]

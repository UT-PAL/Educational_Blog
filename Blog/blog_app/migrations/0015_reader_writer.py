# Generated by Django 3.1 on 2021-11-17 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0014_auto_20211117_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='reader_writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader', models.CharField(max_length=255)),
                ('writer', models.CharField(max_length=255)),
            ],
        ),
    ]
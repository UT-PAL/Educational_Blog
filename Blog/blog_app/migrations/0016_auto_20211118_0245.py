# Generated by Django 3.1 on 2021-11-17 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0015_reader_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader_writer',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reader_writer',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to=settings.AUTH_USER_MODEL),
        ),
    ]
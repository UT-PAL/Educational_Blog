# Generated by Django 3.1 on 2021-11-17 16:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='review_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviews',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_blog', to='blog_app.blog'),
        ),
    ]
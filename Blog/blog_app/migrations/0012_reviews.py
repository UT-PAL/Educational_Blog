# Generated by Django 3.1 on 2021-11-17 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0011_blog_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=255)),
                ('rating', models.CharField(choices=[('5 star', '*****'), ('4 star', '****'), ('3 star', '***'), ('2 star', '**'), ('1 star', '*')], default='5 star', max_length=255)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_blog', to='blog_app.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

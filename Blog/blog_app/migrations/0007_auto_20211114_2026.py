# Generated by Django 3.1 on 2021-11-14 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_auto_20211114_0259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shared_post',
            options={'ordering': ('-shared_date',)},
        ),
        migrations.RenameField(
            model_name='shared_post',
            old_name='shared_blog',
            new_name='blog',
        ),
        migrations.RenameField(
            model_name='shared_post',
            old_name='blog_sharer',
            new_name='user',
        ),
    ]

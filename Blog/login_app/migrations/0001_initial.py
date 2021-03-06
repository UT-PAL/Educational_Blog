# Generated by Django 3.1 on 2021-11-21 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile', serialize=False, to='auth.user')),
                ('profile_pic', models.ImageField(upload_to='profile_pics')),
                ('dob', models.DateField(blank=True, null=True)),
                ('facebook_profile', models.URLField(blank=True)),
                ('github_profile', models.URLField(blank=True)),
                ('linkedin_profile', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('EEE', 'EEE'), ('ECE', 'ECE'), ('MTE', 'MTE'), ('ME', 'ME'), ('BECM', 'BECM'), ('CFPE', 'CFPE'), ('CIVIL', 'CIVIL'), ('EETE', 'EETE'), ('GCE', 'GCE'), ('IPE', 'IPE'), ('URP', 'URP'), ('ARCHITECTURE', 'ARCHITECTURE')], default='CSE', max_length=100)),
                ('nid_front', models.ImageField(help_text='Upload front part of your NID card ', upload_to='NID_pics')),
                ('nid_back', models.ImageField(upload_to='NID_pics', verbose_name='Upload back part of your NID card ')),
                ('profile_picture', models.ImageField(null=True, upload_to='teacher_pics', verbose_name='Upload your photo ')),
                ('university', models.CharField(choices=[('RUET', 'RUET'), ('BUET', 'BUET'), ('KUET', 'KUET'), ('CUET', 'CUET'), ('BUTEX', 'BUTEX'), ('DU', 'DU'), ('SUST', 'SUST')], max_length=100)),
                ('nid_number', models.CharField(max_length=10, verbose_name='NID Number: xxx xxx xxxx ')),
                ('email', models.EmailField(max_length=20)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(help_text='Ask a question', max_length=50000)),
                ('problem_picture', models.ImageField(blank=True, help_text='upload your problem picture', upload_to='problem_pictures')),
                ('category', models.CharField(choices=[('CSE', 'CSE'), ('EEE', 'EEE'), ('ECE', 'ECE'), ('MTE', 'MTE'), ('ME', 'ME'), ('BECM', 'BECM'), ('CFPE', 'CFPE'), ('CIVIL', 'CIVIL'), ('EETE', 'EETE'), ('GCE', 'GCE'), ('IPE', 'IPE'), ('URP', 'URP'), ('ARCHITECTURE', 'ARCHITECTURE')], default='CSE', help_text='Select a category', max_length=200)),
                ('question_date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-question_date',),
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('msg', models.CharField(max_length=255)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_date', models.DateField(auto_now_add=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(help_text='Give your valuable answer', max_length=50000)),
                ('solution', models.ImageField(blank=True, help_text='Upload a solution file', upload_to='solution_pics')),
                ('ans_date', models.DateTimeField(auto_now_add=True)),
                ('question1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question1', to='login_app.questions')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='login_app.teacher')),
            ],
            options={
                'ordering': ('-ans_date',),
            },
        ),
    ]

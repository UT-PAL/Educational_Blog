from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from Blog import settings
# Create your models here.
#built-in user model
class User_profile(models.Model):
    user=models.OneToOneField(User,primary_key=True, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics',help_text="Please upload your photo",blank=True)
    dob = models.DateField(null=True)
    facebook_profile = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        User_profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.user_profile.save()


class Follow (models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Follower')
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Following')
    following_date= models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.follower)

class Messages (models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Sender')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Receiver')
    date= models.DateTimeField(auto_now_add=True)
    msg = models.CharField(max_length=255)
    file = models.ImageField(upload_to='msgpics',help_text="Send a file or image " ,blank=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.msg


class Teacher(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name="teacher",null=True)
    teacher_name = models.CharField(max_length=100,null=False)
    choice = (
        ('CSE', 'CSE'),
        ('EEE','EEE'),
        ('ECE','ECE'),
        ('MTE','MTE'),
        ('ME','ME'),
        ('BECM','BECM'),
        ('CFPE','CFPE'),
        ('CIVIL','CIVIL'),
        ('EETE','EETE'),
        ('GCE','GCE'),
        ('IPE','IPE'),
        ('URP','URP'),
        ('ARCHITECTURE','ARCHITECTURE'),
    )
    department = models.CharField(choices=choice,default='CSE',null=False,max_length=100)
    nid_front = models.ImageField(upload_to='NID_pics',null=False,help_text='Upload front part of your NID card ')
    nid_back = models.ImageField(upload_to='NID_pics',null=False,verbose_name='Upload back part of your NID card ')
    profile_picture = models.ImageField(upload_to='teacher_pics',null=True,verbose_name='Upload your photo ')
    varsity_choice=(
        ('RUET','RUET'),
        ('BUET','BUET'),
        ('KUET','KUET'),
        ('CUET','CUET'),
        ('BUTEX','BUTEX'),
        ('DU','DU'),
        ("SUST",'SUST')

    )
    university = models.CharField(choices=varsity_choice,null=False,max_length=100)
    nid_number = models.CharField(max_length=10,null=False,verbose_name='NID Number: xxx xxx xxxx ')
    email = models.EmailField(max_length=20,null=False)

    def __str__(self):
        return self.email


class Questions(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name="students",null=True)
    question_date = models.DateTimeField(auto_now_add=True)
    question = models.TextField(max_length=50000,help_text="Ask a question",null=False)
    problem_picture = models.ImageField(upload_to="problem_pictures",help_text="upload your problem picture",blank=True)
    choice=(
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
        ('ECE', 'ECE'),
        ('MTE', 'MTE'),
        ('ME', 'ME'),
        ('BECM', 'BECM'),
        ('CFPE', 'CFPE'),
        ('CIVIL', 'CIVIL'),
        ('EETE', 'EETE'),
        ('GCE', 'GCE'),
        ('IPE', 'IPE'),
        ('URP', 'URP'),
        ('ARCHITECTURE', 'ARCHITECTURE'),
    )
    category=models.CharField(max_length=200,choices=choice,default='CSE',null=False,help_text="Select a category")


    class Meta:
        ordering = ('-question_date',)



class Answer(models.Model):

    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='teacher',null=True)
    question1 = models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='question1',null=True)
    answer = models.CharField(max_length=50000,help_text="Give your valuable answer")
    ans_date = models.DateTimeField(auto_now_add=True)
    solution = models.ImageField(upload_to='solution_pics',help_text="Upload a solution file",blank=True)


    class Meta:
        ordering = ('-ans_date',)


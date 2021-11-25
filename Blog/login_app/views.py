from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from login_app.forms import SignUpForm, UserProfileChange, Question_form, Answer_form
from login_app.models import Follow, User_profile, Messages, Teacher, Questions,Answer
from django.contrib.auth.models import User
from login_app.forms import EditInfo,Message_form,Teacher_form

from blog_app.models import Blog
# Create your views here.


def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            form.save()
            registered = True


    dict = {'form':form,'registered':registered}
    return render(request, 'login_app/signup.html', context=dict)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                online = User_profile.objects.get(user=user)
                online.is_online = True
                online.save()

                return HttpResponseRedirect(reverse('index'))
    return render(request, 'login_app/login.html', context={'form':form})

@login_required
def logout_user(request):
    offline = User_profile.objects.get(user=request.user)
    offline.is_online = False
    offline.save()
    logout(request)

    return HttpResponseRedirect(reverse('index'))

@login_required
def teacher_profile(request):
    current_user = request.user
    teacher = Teacher.objects.get(user=current_user)
    return render(request, 'login_app/teacher_profile.html', context={'teacher':teacher})

@login_required
def profile(request):
    return render(request, 'login_app/profile.html', context={})

def show_followers(request):
    follower_list = Follow.objects.filter(following=request.user)
    return render(request, 'login_app/follower_and_following.html', context={'list': follower_list})

def show_following(request):
    following_list = Follow.objects.filter(follower=request.user)
    return render(request, 'login_app/follower_and_following.html', context={'list1':following_list})


@login_required
def user_change(request):
    current_user = User.objects.get(username=request.user)
    form = UserProfileChange(instance=current_user)

    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)

        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)

            return HttpResponseRedirect(reverse('login_app:profile'))

    return render(request, 'login_app/change_profile.html', context={'form':form})


@login_required
def edit_othersInfo(request):
    current_user = User_profile.objects.get(user=request.user)
    form1= EditInfo(instance=current_user)
    if request.method == 'POST':
        form1= EditInfo(request.POST,request.FILES,instance=current_user)
        if form1.is_valid():
            form1.save(commit=True)
            form1 = EditInfo(instance=current_user)

            return HttpResponseRedirect(reverse('login_app:profile'))
    return render(request, 'login_app/edit_othersInfo.html', context={'form1':form1})



@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'login_app/pass_change.html', context={'form':form, 'changed':changed})


def user(request,username):
    other_user = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user,following=other_user)
    blogs = Blog.objects.filter(author=other_user)
    dict={'other_user':other_user,'already_followed':already_followed,'blogs':blogs}
    if other_user == request.user:
        return HttpResponseRedirect(reverse('login_app:profile'))
    return render(request,'login_app/other_user.html',context=dict)

def follow (request,username):
    following_user = User.objects.get(username=username)
    follower_user = User.objects.get(username=request.user)
    already_followed = Follow.objects.filter(follower=follower_user,following=following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user,following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('login_app:other_user',kwargs={'username':username}))

@login_required
def unfollow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = User.objects.get(username=request.user)
    already_followed = Follow.objects.filter(follower=follower_user,following=following_user)
    already_followed.delete()
    return  HttpResponseRedirect(reverse('login_app:other_user',kwargs={'username':username }))

@login_required
def chat_list(request):
    all_user = User_profile.objects.filter(is_online=True)
    offline_user = User_profile.objects.filter(is_online=False)
    return render(request,'chat/chat_list.html',context={'offline_users':offline_user,'all_user':all_user})

@login_required
def change_active_status(request):
    user = User_profile.objects.get(user=request.user)
    if user.is_online == True:
        user.is_online=False
        user.save()
        return HttpResponseRedirect(reverse('login_app:profile'))

    else :
        user.is_online=True
        user.save()
        return HttpResponseRedirect(reverse('login_app:profile'))


@login_required
def chat_view(request,username):
    user = User.objects.get(username=username)

    s_msg = Messages.objects.filter(sender=request.user,receiver=user)
    r_msg = Messages.objects.filter(receiver=request.user,sender=user)
    msg =s_msg|r_msg
    M_form = Message_form()
    if request.method =='POST':
        M_form = Message_form(request.POST,request.FILES)
        if M_form.is_valid():
            form = M_form.save(commit=False)
            form.sender = request.user
            form.receiver = user
            form.save()
            return HttpResponseRedirect(reverse('login_app:chat',kwargs={'username':username}))

    return render (request,'chat/chat.html', context={'M_form':M_form,'msg':msg})



@login_required
def delete_profile(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                 user.is_active=False
                 user.save()
                 return render (request,'login_app/login.html',context={'user':user})
    return render (request,'login_app/delete_profile.html',context={'form':form})



@login_required
def teacher(request):
    teacher = request.user
    teacher_form = Teacher_form(instance=teacher)

    if request.method == 'POST':
        teacher_form = Teacher_form(request.POST,request.FILES)
        if teacher_form.is_valid():
            form = teacher_form.save(commit=False)
            form.user= teacher
            form.save()
            teacher.is_staff=True
            teacher.save()

            return HttpResponseRedirect(reverse('login_app:teacher_profile'))
    return render(request, 'login_app/teacher_form.html', context={'form':teacher_form})



@login_required
def Ask_question(request):
    form = Question_form()
    user = request.user
    if request.method=='POST':
        form = Question_form(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.student = user
            f.save()
            return HttpResponseRedirect(reverse('login_app:answer'))
    return render(request,'question_app/question_ans.html',context={'form':form})

@login_required
def question_feed(request):
    form = Answer_form()
    all_ques = Questions.objects.all()
    return render(request,'question_app/question_feed.html',context={'all_ques':all_ques,'form':form})

@login_required
def ans_question(request,pk):
    ques = Questions.objects.get(pk=pk)
    teacher = Teacher.objects.get(user=request.user)
    form = Answer_form()
    if request.method =='POST':
        form =Answer_form(request.POST,request.FILES)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.question1 = ques
            ans.teacher= teacher
            ans.save()
            return HttpResponseRedirect(reverse('login_app:answer_details',kwargs={'pk':pk}))

    return render(request,'question_app/ans_feed.html',context={'ques':ques,'form':form})

def ans_feed(request,pk):
    question = Questions.objects.get(pk=pk)
    ans = Answer.objects.filter(question1=question)
    return render(request,'question_app/answer_details.html',context={'question':question,'ans':ans})
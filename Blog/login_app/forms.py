from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from login_app.models import User_profile, Messages, Teacher, Questions, Answer


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


class EditInfo(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ('profile_pic','dob','facebook_profile','github_profile','linkedin_profile')


class Message_form(forms.ModelForm):
    class Meta:
        model = Messages
        fields=('msg','file')


class Teacher_form(forms.ModelForm):
    class Meta:
        model= Teacher
        fields=('teacher_name','department','university','email','nid_number','nid_front','nid_back','profile_picture',)

class Question_form(forms.ModelForm):
    class Meta:
        model=Questions
        fields=('question','problem_picture','category')


class Answer_form(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer', 'solution')

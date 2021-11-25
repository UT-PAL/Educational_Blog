from django import forms
from blog_app.models import Blog, Comment,shared_post,Reviews


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class SharedForm(forms.ModelForm):
    class Meta:
        model = shared_post
        fields = ('whats_on_mind',)

class Review_form(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('review','rating',)
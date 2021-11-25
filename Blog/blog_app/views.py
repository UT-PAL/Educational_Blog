from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DetailView,View,TemplateView,DeleteView
from django.contrib.auth.models import User
from login_app.models import User_profile
from blog_app.models import Blog, Comment, Likes, Dislikes,shared_post,Reviews,Reader
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog_app.forms import CommentForm,SharedForm,Review_form
import uuid
from django.db.models import Avg

# Create your views here.
class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'blog_app/my_blogs.html'

class MyBlogs1(LoginRequiredMixin,TemplateView):
    template_name = 'login_app/profile.html'



class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_app/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image','blog_reference')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'blog_app/blog_list.html'



@login_required
def filter(request):
    blog=Blog.objects.all()
    return render (request,'blog_app/filtered_blog.html',context={'blog':blog})

@login_required
def filtered_blog(request,tag):
    f_blog=Blog.objects.filter(tags=tag)
    return render(request, 'blog_app/filtered_bloglist.html', context={'f_blog': f_blog})


@login_required
def shared_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    user = request.user
    shared_form = SharedForm()
    already_liked = Likes.objects.filter(blog=blog, user=request.user)
    already_disliked = Dislikes.objects.filter(blog=blog, user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    if already_disliked:
        disliked = True
    else:
        disliked = False
    if request.method == 'POST':
        shared_form = SharedForm(request.POST)
        if shared_form.is_valid():
            share = shared_form.save(commit=False)
            share.user = request.user
            share.blog = blog
            share.save()
            return HttpResponseRedirect(reverse('blog_app:my_shared_blogs'))
    return render(request, 'blog_app/shared_blog.html', context={'blog':blog, 'shared_form':shared_form, 'user':user,'liked':liked,'disliked':disliked,'liker':already_liked,'disliker':already_disliked})

@login_required
def my_shared_blogs(request):
    posts = shared_post.objects.filter(user=request.user)
    return render(request,"blog_app/my_shared_blogs.html",context={'posts':posts})

@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Likes.objects.filter(blog=blog, user= request.user)
    already_disliked = Dislikes.objects.filter(blog=blog,user=request.user)
    r = Reviews.objects.filter(blog=blog).aggregate(avg_review=Avg('rating'))
    if already_liked:
        liked = True
    else:
        liked = False
    if already_disliked:
        disliked = True
    else:
        disliked=False


    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('blog_app:blog_details', kwargs={'slug':slug}))
    return render(request, 'blog_app/blog_details.html', context={'blog':blog, 'comment_form':comment_form,'r':r, 'liked':liked,'disliked':disliked,'liker':already_liked})

@login_required
def delete_blogs(request,slug):
    blog=Blog.objects.filter(slug=slug)
    b=blog.delete()
    return render(request,"blog_app/my_blogs.html",context={'blog':blog,'b':b})
@login_required
def delete_shared_blogs(request,slug):
    blog1 = Blog.objects.get(slug=slug)
    shared_blog = shared_post.objects.filter(blog=blog1)
    s = shared_blog.delete()
    return render(request, "blog_app/my_shared_blogs.html", context={'blog1': blog1, 's': s})


@login_required
def likes(request,slug):
    blog=Blog.objects.get(slug=slug)
    user=User.objects.all()

    liker=Likes.objects.filter(user__id__in=user,blog=blog)

    return render(request,"blog_app/likes.html",context={"liker":liker})

@login_required
def dislikes(request,slug):
    blog=Blog.objects.get(slug=slug)
    user=User.objects.all()
    disliker=Dislikes.objects.filter(user__id__in=user,blog=blog)

    return render(request,"blog_app/likes.html",context={'disliker':disliker})



@login_required
def liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    if not already_liked:
        liked_post = Likes(blog=blog, user=user)
        liked_post.save()

    return HttpResponseRedirect(reverse('blog_app:blog_details', kwargs={'slug':blog.slug}))

@login_required
def unliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('blog_app:blog_details', kwargs={'slug':blog.slug}))

@login_required
def dislike(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_disliked = Dislikes.objects.filter(blog=blog, user=user)
    if not already_disliked:
        disliked_post = Dislikes(blog=blog, user=user)
        disliked_post.save()
    return HttpResponseRedirect(reverse('blog_app:blog_details', kwargs={'slug':blog.slug}))

@login_required
def disliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_disliked = Dislikes.objects.filter(blog=blog, user=user)
    already_disliked.delete()
    return HttpResponseRedirect(reverse('blog_app:blog_details', kwargs={'slug':blog.slug}))



class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'blog_app/edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('blog_app:blog_details', kwargs={'slug':self.object.slug})

@login_required
def search(request):
    if request.method == 'POST':
        username= request.POST.get('search')
        request_username = User.objects.filter(username__icontains=username)
        blogs = Blog.objects.filter(slug__icontains=username)
    return render(request,'blog_app/search.html',context={'keyword':username,'request_username':request_username,'blogs':blogs})

@login_required
def review_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    review_form = Review_form()
    already_reviewed = Reviews.objects.filter(blog=blog, user=request.user)
    review = Reviews.objects.filter(blog=blog)
    r = review.aggregate(avg_review=Avg('rating'))
    if already_reviewed:
        reviewed = True
    else:
        reviewed = False
    if request.method == 'POST':
        review_form= Review_form(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.blog = blog
            review.save()
            return HttpResponseRedirect(reverse('blog_app:review_detail', kwargs={'slug': slug}))
    return render(request, 'blog_app/blog_details.html',context={'already_reviewed':already_reviewed,'review':review,'blog': blog, 'review_form': review_form, 'r':r,'reviewed': reviewed, })


@login_required
def review_now(request, slug):
    blog = Blog.objects.get(slug=slug)
    user = request.user
    already_reviewed = Reviews.objects.filter(blog=blog, user=user)
    if not already_reviewed:
        reviewed_post = Reviews(blog=blog, user=user)
        reviewed_post.save()
    return HttpResponseRedirect(reverse('blog_app:review_details', kwargs={'slug':slug}))

@login_required
def not_review(request, slug):
    blog = Blog.objects.get(slug=slug)
    user = request.user
    already_reviewed= Reviews.objects.filter(blog=blog, user=user)
    already_reviewed.delete()
    return HttpResponseRedirect(reverse('blog_app:review_details', kwargs={'slug':slug}))



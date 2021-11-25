from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views
app_name='login_app'
urlpatterns = [
 path('signup/', views.sign_up,name='signup'),
 path('login/',views.login_page, name='login'),
 path('logout/',views.logout_user, name='logout'),
 path('profile/', views.profile, name='profile'),
 path('active_status/',views.change_active_status,name='change_active_status'),
 path('teacher_profile/', views.teacher_profile, name='teacher_profile'),

 path('show_follower/',views.show_followers,name='show_follower'),
 path('show_following/',views.show_following,name='show_following'),
 path('change_profile/', views.user_change, name='change_profile'),
 path('password/', views.pass_change, name='pass_change'),

 path('edit/',views.edit_othersInfo,name='edit_othersInfo'),

path('other_user/<username>/',views.user, name='other_user'),
 path('follow/<username>/',views.follow,name='follow'),
 path ('unfollow/<username>',views.unfollow,name='unfollow'),

path('chat/<username>',views.chat_view,name='chat'),
path('chat_list/',views.chat_list,name='chat_list'),

path('delete/',views.delete_profile,name='delete_profile'),
 path('teacher/',views.teacher,name='teacher'),
path('Ask_a_question/', views.Ask_question, name='question'),
    path('question/', views.question_feed, name='answer'),
    path('ans_question/<pk>', views.ans_question, name='answer_question'),
    path('ans_details/<pk>', views.ans_feed, name='answer_details')




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
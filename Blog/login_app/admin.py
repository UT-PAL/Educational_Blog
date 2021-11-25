from django.contrib import admin

# Register your models here.
from login_app.models import User_profile,Follow,Messages,Teacher,Questions,Answer
admin.site.register(User_profile)
admin.site.register(Follow)
admin.site.register(Messages)
admin.site.register(Teacher)
admin.site.register(Questions)
admin.site.register(Answer)

from django.contrib import admin
from .models import MsUser, TempMsUser, Post, Comment, Like

# Register your models here.
admin.site.register(MsUser)
admin.site.register(TempMsUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
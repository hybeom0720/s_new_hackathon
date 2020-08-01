from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MsUser(models.Model):
    user = models.TextField() 
    name = models.TextField()
    kisoo = models.IntegerField(null = True, blank = True)
    email = models.TextField()
    major = models.TextField()
    idNumber = models.IntegerField()
    authority = models.TextField()


class TempMsUser(models.Model):
    name = models.TextField()
    kisoo = models.IntegerField(null = True, blank = True)
    email = models.TextField()
    major = models.TextField()
    idNumber = models.IntegerField()


BOARD_TYPE = (
    ("1", "공지사항"),
    ("2", "세션")
)

class Post(models.Model):
    title = models.CharField(max_length =200)
    content = models.TextField()
    author = models.ForeignKey(MsUser, on_delete = models.CASCADE, related_name = 'posts')
    category = models.CharField(max_length = 10, choices = BOARD_TYPE, default = '공지사항')
   

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    content = models.TextField()
    author = models.ForeignKey(MsUser, on_delete = models.CASCADE, related_name = 'comments')

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'likes')
    user = models.ForeignKey(MsUser, on_delete = models.CASCADE, related_name = 'likes')


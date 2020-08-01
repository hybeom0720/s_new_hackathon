from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MsUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = False)
    name = models.TextField()
    kisoo = models.IntegerField(null = True, blank = True)
    address = models.TextField()
    major = models.TextField()
    idNumber = models.IntegerField()
    authority = models.TextField()


class Post(models.Model):
    title = models.Charfield(max_length =200)
    content = models.TextField()
    author = models.ForeignKey(MsUser, on_delete = models.CASCADE, related_name = 'posts')
    cover = models.ImageField(upload_to = 'images/', null = True, blank = True)

    def __str__(self):
        return self.title

    
class Comment(models.Model):
    post = models.foreignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    content = models.TextField()
    author = models.ForeignKey(MsUser, on_delete = models.CASCADE, related_name = 'comments')

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_anem = 'likes')
    user = models.ForeignKey(MsUser, on_delete = models.CASCADE, related_name = 'likes')


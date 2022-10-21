from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.URLField(max_length=300)
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def comment_count(self):
        return self.comment_set.all().count()

    def like_count(self):
        return self.like_set.all().count()

    def view_count(self):
        return self.postview_set.all().count()

    def comments(self):
        return self.comment_set.all()


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username


class Like(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by.username


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username

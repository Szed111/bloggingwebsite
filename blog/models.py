from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete tells django what to do once a post is deleted
    # it means that we delete the posts of the User once a User is deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    # reverse function returns the string to the route


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.post.pk})


class ImpLink(models.Model):
    link_title = models.CharField(max_length=100)
    link_format = models.TextField()

    def __str__(self):
        return "LinkTile {}".format(self.link_title)

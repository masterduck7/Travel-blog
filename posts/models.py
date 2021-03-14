import json

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    username = models.CharField(max_length=200, blank=False, null=False, default="")

    def __str__(self):
        return self.title

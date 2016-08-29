# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User)
    nationality = models.CharField(max_length=32,
                                   default="")

    def __str__(self):
        return self.user.get_username()


class Post(models.Model):
    title = models.CharField('Titulo', max_length=32)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # photo = models.ImageField(upload_to="media/", blank=True)
    publicated = models.BooleanField()
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    comment = models.TextField()
    post = models.ForeignKey(Post)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField()

    def __str__(self):
        return self.comment

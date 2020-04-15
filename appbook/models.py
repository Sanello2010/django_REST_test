from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # send book


class Comment(models.Model):
    comment_book = models.ForeignKey(Book,
                                     on_delete=models.CASCADE,
                                     related_name="comment")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

# Create your models here.

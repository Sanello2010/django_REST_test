from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_book = models.ForeignKey(Book,
                                     on_delete=models.CASCADE,
                                     related_name="comment")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

# Create your models here.

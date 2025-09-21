from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default="Unknown Author")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

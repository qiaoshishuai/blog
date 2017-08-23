from django.db import models


# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.name + self.text[:20]

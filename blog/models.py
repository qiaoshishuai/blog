from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)  # 标题

    body = models.TextField()  # 内容

    create_time = models.DateTimeField()  # 创建时间

    modified_time = models.DateTimeField()  # 修改时间

    excerpt = models.CharField(max_length=250, blank=True)  # 摘要

    category = models.ForeignKey(Category)  # 分类 一对多关系

    tags = models.ManyToManyField(Tag, blank=True)  # 标签 多对多关系

    author = models.ForeignKey(User)  # 作者 一对多关系

    def __str__(self):
        return 'title:%s-create_time:%s-category:%s-tags:%s-author:%s' % (
            self.title, self.create_time, self.category, self.tags, self.author)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

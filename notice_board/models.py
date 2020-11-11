from django.conf import settings
from django.db import models
from django.utils import timezone


class University(models.Model):
    """
    大学
    - ユーザーは一つの大学に所属する

    name:大学名
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Thread(models.Model):
    """
    スレッド（掲示板）
    - 各大学は0個以上のスレッドを持つ

    university_id:大学のid
    author:作成者
    title:スレッド名
    created_date:作成日
    """
    university_id = models.ForeignKey('University', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.university_id

class Post(models.Model):
    """
    投稿
    - 各スレッドは0個以上の投稿を持つ

    thread_id:スレッドのid
    author:投稿者
    title:スレッド名
    published_date:投稿日
    """
    thread_id = models.ForeignKey('Thread', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.thread_id

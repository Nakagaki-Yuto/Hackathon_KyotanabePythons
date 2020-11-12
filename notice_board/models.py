from django.conf import settings
from django.db import models
from django.utils import timezone

GRADE＿CHOICES = (
    ('1', '学部1年'),
    ('2', '学部2年'),
    ('3', '学部3年'),
    ('4', '学部4年'),
    ('5', '修士1年'),
    ('6', '修士2年'),
)
GENDER_CHOICES = (
    ('1', '女性'),
    ('2', '男性'),
)


class UserProfile(models.Model):
    """
    ユーザープロフィール
    - 各ユーザは一つのプロフィールを持つ

    user:対応するユーザー
    university:大学名
    grade:学年
    gender:性別
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    grade = models.CharField("学年", max_length=6, choices=GRADE_CHOICES, blank=True)
    gender = models.CharField("性別", max_length=2, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return self.user.username


class University(models.Model):
    """
    大学

    name:大学名
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Thread(models.Model):
    """
    スレッド（掲示板）

    university:属している大学
    author:作成者
    title:スレッド名
    created_date:作成日
    """
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    投稿
    - 各スレッドは0個以上の投稿を持つ

    thread:属しているスレッド
    author:投稿者
    title:スレッド名
    published_date:投稿日
    """
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

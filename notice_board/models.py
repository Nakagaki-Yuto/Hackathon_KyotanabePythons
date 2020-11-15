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
    mail = models.EmailField(max_length=70)
    grade = models.CharField("学年", max_length=6, choices=GRADE_CHOICES, blank=True)
    gender = models.CharField("性別", max_length=2, choices=GENDER_CHOICES, blank=True)
    is_university = models.BooleanField("大学様用アカウント", default=False)

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
    category:カテゴリー名
    """
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    投稿
    - 各スレッドは0個以上の投稿を持つ

    thread:属しているスレッド
    author:投稿者
    text:投稿内容
    published_date:投稿日
    """
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Category(models.Model):
    """
    カテゴリー
    
    name:カテゴリー名
    """
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Report(models.Model):
    """
    レポート

    university:大学名
    category:カテゴリー
    word:単語
    content:レポート内容
    """
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    word = models.CharField(max_length=1000)
    content = models.IntegerField(default=0)

    def __str__(self):
        return self.word
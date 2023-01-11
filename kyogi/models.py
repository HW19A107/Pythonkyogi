from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# ユーザーアカウントのモデルクラス
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username


class total(models.Model):
    name = models.CharField(max_length=255,null=True)
    number = models.IntegerField(null=True)
    clear = models.CharField(max_length=255,null=True)
    clear_time = models.CharField(max_length=255,null=True)
    datetime = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'number', 'clear'], name='unique_total')
        ]


class resets(models.Model):
    name = models.CharField(max_length=255,null=True)
    number = models.IntegerField(null=True)
    save_time = models.CharField(max_length=255,null=True)


class anker(models.Model):
    anktext = models.CharField(max_length=255,null=False)
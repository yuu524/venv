from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    user_id = models.CharField(
        max_length=36,
        unique=True,
        editable=False,
        verbose_name='ユーザーID'
    )
    email = models.EmailField(unique=True, verbose_name='メールアドレス')
    language = models.CharField(
        max_length=10,
        choices=[
            ('ja', '日本語'),
            ('en', 'English'),
            ('es', 'Español'),
        ],
        default='ja',
        verbose_name='言語設定'
    )

    REQUIRED_FIELDS = ['email', 'language']
    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        if not self.user_id:  # 初回保存時のみ生成
            self.user_id = str(uuid.uuid4())  # UUIDを生成
        super().save(*args, **kwargs)

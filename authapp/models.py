from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, User

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar', blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='возраст')

    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url


    def __str__(self):
        return self.username


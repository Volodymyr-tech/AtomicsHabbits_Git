from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to="users/avatars/", blank=True, null=True
    )
    username = models.CharField(
        max_length=155, null=True, blank=True, verbose_name="Username"
    )
    city = models.CharField(
        max_length=20,
        verbose_name="Where do you live?",
        help_text="Choose a city",
        null=True,
        blank=True,
    )
    tg_chat_id = models.CharField(
        max_length=155, null=True, blank=True, verbose_name="Telegram chat ID"
    )

    objects = CustomUserManager()  # Используем кастомный менеджер

    USERNAME_FIELD = "email"  # Указываем email вместо username
    REQUIRED_FIELDS = [
        "username",
    ]  # Поля, которые нужно запросить при создании суперюзера

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

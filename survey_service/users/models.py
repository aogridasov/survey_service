from django.contrib.auth.models import AbstractUser
from django.db import models


class UserCompletedSurveyManager(models.Manager):
    """Кастомный менеджер для модели User"""
    def get_queryset(self):
        """Дополняем запрос к дб"""
        return super().get_queryset().select_related(
            'coins',
            'upgrades'
        ).annotate(completed=models.Count('completed_surveys'))


class User(AbstractUser):
    """Модель пользователя"""
    username = models.CharField(
        max_length=20,
        unique=True,
    )

    objects = UserCompletedSurveyManager()


class Coins(models.Model):
    """Модель валюты для пользователей. Кошелек."""
    value = models.SmallIntegerField(
        verbose_name='Количество',
        default=0
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='coins'
    )

    class Meta:
        verbose_name = 'Монетки'

    def __str__(self):
        return f'Баланс {self.user}: {self.value}'


class Upgrades(models.Model):
    """Модель для отображения косметических покупок пользователя"""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='upgrades'
    )
    background_color = models.BooleanField(default=False)
    username_border = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Апгрейды'

    def __str__(self):
        return f'Апгрейды {self.user}'

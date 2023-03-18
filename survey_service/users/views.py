from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import upgrades_cfg
from .forms import CreationForm
from .models import User


class SignUp(CreateView):
    """Базовая вью для регистрации"""
    form_class = CreationForm
    success_url = reverse_lazy('surveys:index')
    template_name = 'users/signup.html'


def buy_background(request, user_id):
    """Обрабатывает нажатие кнопки покупки бэкграунда"""
    user = User.objects.select_related('coins', 'upgrades').get(id=user_id)
    coins = user.coins
    upgrades = user.upgrades
    if coins.value >= upgrades_cfg.BACKGROUND_COLOR_PRICE and not upgrades.background_color:
        upgrades.background_color = True
        coins.value -= upgrades_cfg.BACKGROUND_COLOR_PRICE
        upgrades.save()
        coins.save()
    return redirect('surveys:user_profile', user_id=user_id)


def buy_border(request, user_id):
    """Обрабатывает нажатие кнопки покупки рамки"""
    user = User.objects.select_related('coins', 'upgrades').get(id=user_id)
    coins = user.coins
    upgrades = user.upgrades
    if coins.value >= upgrades_cfg.BORDER_PRICE and not upgrades.username_border:
        upgrades.username_border = True
        coins.value -= upgrades_cfg.BORDER_PRICE
        upgrades.save()
        coins.save()
    return redirect('surveys:user_profile', user_id=user_id)

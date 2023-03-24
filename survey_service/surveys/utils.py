from django.conf import settings
from django.core.paginator import Paginator

from users.models import Coins
from users.upgrades_cfg import (BACKGROUND_COLOR_CODE, BACKGROUND_COLOR_PRICE,
                                BORDER_CODE, BORDER_PRICE)


def paginator(obj_list, request):
    """Реализует паджинацию для переданного списка объектов"""
    paginator = Paginator(obj_list, settings.SURVEYS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def give_user_coins(survey, user):
    """Начисляет переданному пользователю количество
    монеток в соответствии с ценой переданного опроса"""
    coins = Coins.objects.get(user=user)
    coins.value += survey.coins_value
    coins.save()


def get_profile_bg_color(user):
    """Возвращает код цвета бэкграунда профиля
    в зависимости от апгрейдов пользователя"""
    if user.upgrades.background_color:
        return BACKGROUND_COLOR_CODE
    return ''


def get_profile_border(user):
    """Возвращает код рамки профиля
    в зависимости от апгрейдов пользователя"""
    if user.upgrades.username_border:
        return BORDER_CODE
    return ''


def get_upgrades_styles_all(context):
    """Дополняет контекст информацией о стилях ВСЕХ апгрейдов"""
    context.update({
        'background_color': BACKGROUND_COLOR_CODE,
        'border': BORDER_CODE,
    })
    return context


def get_upgrades_context(context):
    """Дополняет контекст информацией об апгрейдах"""
    user = context['profile_user']
    context.update({
        'background_color': get_profile_bg_color(user),
        'border': get_profile_border(user),
        'bg_color_price': BACKGROUND_COLOR_PRICE,
        'border_price': BORDER_PRICE,
    }
    )
    return context

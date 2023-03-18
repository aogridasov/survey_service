from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from users.models import User

from .forms import SurveyForm
from .models import CompletedSurvey, Survey
from .utils import (get_upgrades_context, get_upgrades_styles_all,
                    give_user_coins, paginator)


def index(request):
    """Отображает главную страницу"""
    survey_list = Survey.objects.all()
    page_obj = paginator(survey_list, request)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'surveys/index.html', context)


def user_profile(request, user_id):
    """Отображает профиль пользователя"""
    user = get_object_or_404(User, pk=user_id)
    completed_survey_list = CompletedSurvey.objects.filter(
        user=user
    ).prefetch_related('survey')
    survey_list = [
        complited_survey.survey for complited_survey in completed_survey_list
    ]
    page_obj = paginator(survey_list, request)

    context = {
        'user': user,
        'page_obj': page_obj,
    }
    get_upgrades_context(context)
    return render(request, 'surveys/user_profile.html', context)


def survey_page(request, survey_id):
    """Отображает страницу опроса"""
    survey = get_object_or_404(Survey, pk=survey_id)
    context = {
        'survey': survey,
        'form': SurveyForm(survey=survey, user=request.user)
    }
    return render(request, 'surveys/survey.html', context)


@login_required
def apply_survey(request, survey_id):
    """Обрабатывает нажатие кнопки Отправить на странице опроса
    Сохраняет ответы пользователя в БД"""
    survey = get_object_or_404(Survey, pk=survey_id)
    user = request.user
    form = SurveyForm(request.POST or None, survey=survey, user=user)
    if form.is_valid():
        form.save()
        give_user_coins(survey, user)
        return redirect('surveys:index')
    return render(request, 'surveys/survey.html', {'form': form})


def leaderboard(request):
    """Отображает страницу с рейтингом участников"""
    users = User.objects.annotate(completed=Count('completed_surveys')).order_by('-completed')
    page_obj = paginator(users, request)
    context = {
        'page_obj': page_obj
    }
    get_upgrades_styles_all(context)
    return render(request, 'surveys/leaderboard.html', context)

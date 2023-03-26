from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView
from users.models import User

from .forms import SurveyForm
from .models import Survey
from .utils import (get_upgrades_context, get_upgrades_styles_all,
                    give_user_coins)


class IndexView(ListView):
    """Отображает главную страницу"""
    model = Survey
    paginate_by = settings.SURVEYS_PER_PAGE
    template_name = 'surveys/index.html'


class LeaderboardView(ListView):
    """Отображает главную страницу"""
    queryset = User.objects.order_by('-completed')
    paginate_by = settings.USERS_PER_PAGE
    template_name = 'surveys/leaderboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_upgrades_styles_all(context)
        return context


class UserDetailView(SingleObjectMixin, ListView):
    """Отображает профиль пользователя"""
    paginate_by = settings.SURVEYS_PER_PAGE
    template_name = 'surveys/user_profile.html'
    context_object_name = 'profile_user'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=User.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request_user_id'] = self.request.user.id
        get_upgrades_context(context)
        return context

    def get_queryset(self):
        completed = self.object.completed_surveys.prefetch_related('survey')
        return [comp_survey.survey for comp_survey in completed]


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

from django.urls import path

from . import views

app_name = 'surveys'

urlpatterns = [
    path('', views.index, name='index'),
    path('survey/<int:survey_id>/', views.survey_page, name='survey_page'),

    path(
        'survey/<int:survey_id>/apply/',
        views.apply_survey,
        name='apply_survey'
    ),
    path(
        'profile/<int:user_id>/',
        views.user_profile,
        name='user_profile'
    ),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]

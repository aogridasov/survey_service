from django.urls import path

from . import views

app_name = 'surveys'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('survey/<int:survey_id>/', views.survey_page, name='survey_page'),

    path(
        'survey/<int:survey_id>/apply/',
        views.apply_survey,
        name='apply_survey'
    ),
    path(
        'profile/<int:pk>/',
        views.UserDetailView.as_view(),
        name='user_profile'
    ),
    path('leaderboard/', views.LeaderboardView.as_view(), name='leaderboard'),
]

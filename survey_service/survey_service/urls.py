from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('auth/', include('users.urls', namespace='auth')),
    path('', include('surveys.urls', namespace='surveys')),
    path('admin/', admin.site.urls)
]

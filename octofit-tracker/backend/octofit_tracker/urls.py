from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

import os
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        base_url = "/api/"
    return Response({
        'users': f'{base_url}users/',
        'teams': f'{base_url}teams/',
        'activities': f'{base_url}activities/',
        'leaderboard': f'{base_url}leaderboard/',
        'workouts': f'{base_url}workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/users/', views.UserListView.as_view(), name='user-list'),
    path('api/teams/', views.TeamListView.as_view(), name='team-list'),
    path('api/activities/', views.ActivityListView.as_view(), name='activity-list'),
    path('api/leaderboard/', views.LeaderboardListView.as_view(), name='leaderboard-list'),
    path('api/workouts/', views.WorkoutListView.as_view(), name='workout-list'),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from season.views import SeasonListView
from agriculture.views import AgricultureListView, AgricultureTypeListView

app_name = 'api'

urlpatterns = [
    # Agriculture
    path('agriculture/list', AgricultureListView.as_view(), name='agriculture-list'),
    path('agriculture-type/list', AgricultureTypeListView.as_view(),
         name='agriculture-type-list'),

    # Season
    path('season/list', SeasonListView.as_view(), name='season-list'),
]

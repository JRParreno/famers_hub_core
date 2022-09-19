from django.urls import path
from django.contrib.auth import views as auth_views
from agriculture.views import AgricultureListView, AgricultureTypeListView

app_name = 'api'

urlpatterns = [
    path('agriculture/list', AgricultureListView.as_view(), name='agriculture-list'),
    path('agriculture-type/list', AgricultureTypeListView.as_view(),
         name='agriculture-type-list'),
]

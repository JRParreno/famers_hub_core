from django.urls import path
from django.contrib.auth import views as auth_views
from season.views import SeasonListView
from agriculture.views import AgricultureListView, AgricultureTypeListView
from recommendation.views import RecommendationListView, RecommendationDetailView, RecommendationRateView
from farmers_hub_core.views import RegisterView
from community.views import PostCreateView, PostListView

app_name = 'api'

urlpatterns = [
    # community
    path('register', RegisterView.as_view(), name='register'),
    path('post/list', PostListView.as_view(), name='post-list'),
    path('post/create', PostCreateView.as_view(), name='post-create'),

    # Agriculture
    path('agriculture/list', AgricultureListView.as_view(), name='agriculture-list'),
    path('agriculture-type/list', AgricultureTypeListView.as_view(),
         name='agriculture-type-list'),

    # Season
    path('season/list', SeasonListView.as_view(), name='season-list'),

    # Recommendation
    path('recommendation/list', RecommendationListView.as_view(),
         name='recommendation-list'),
    path('recommendation/detail/<pk>', RecommendationDetailView.as_view(),
         name='recommendation-detail'),
    path('recommendation/rate/<pk>', RecommendationRateView.as_view(),
         name='recommendation-rate'),
]

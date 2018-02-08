from django.urls import path

from . import views

urlpatterns = [
    path('', views.ScoreListView.as_view(), name='home'),
    path('score/<pk>/', views.ScoreDetailView.as_view(), name='score_detail'),
    path('myscores/', views.scoreAdminListView, name='score_admin_view'),
    path('new/', views.ScoreCreateView.as_view(), name='new_score'),
    path('score/<pk>/update', views.ScoreUpdateView.as_view(), name='score_update'),
    path('score/<pk>/remove/', views.ScoreDeleteView.as_view(), name='score_delete'),
]

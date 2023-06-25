from django.urls import path
from .views import GamesListView, GamesDetailView


urlpatterns = [
    path('list/', GamesListView.as_view(), name='game_list'),
    path('detail/', GamesDetailView.as_view(), name='game_detail')
]

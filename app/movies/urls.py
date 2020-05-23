from django.urls import path

from .views import MovieListView, MovieDetailView

urlpatterns = [
    path("api/movies/", MovieListView.as_view()),
    path("api/movies/<int:pk>/", MovieDetailView.as_view()),
]

import pytest

from .models import Movie


@pytest.mark.django_db  # explicitly request database access
def test_movie_model():

    def _assert_set():
        assert movie.title == "Raising Arizona"
        assert movie.genre == "comedy"
        assert movie.year == "1987"
        assert movie.created_date
        assert movie.updated_date
        assert str(movie) == movie.title

    movie = Movie(title="Raising Arizona", genre="comedy", year="1987")
    movie.save()
    _assert_set()

    movie = Movie.objects.create(title="Raising Arizona", genre="comedy", year="1987")
    _assert_set()

import pytest
from unittest.mock import MagicMock
from service.director import DirectorDAO
from service.genre import GenreDAO
from service.movie import MovieDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie


@pytest.fixture
def data_for_director_dao():
    director_1 = Director(id=1, name='name_1')
    director_2 = Director(id=2, name='name_2')
    director_3 = Director(id=3, name='name_3')
    director_4 = Director(id=4, name='name_4')
    return {1: director_1, 2: director_2, 3: director_3, 4: director_4}


@pytest.fixture
def director_dao(data_for_director_dao):
    director_dao = DirectorDAO(None)
    director_dao.get_one = MagicMock(side_effect=data_for_director_dao.get)
    director_dao.get_all = MagicMock(return_value=data_for_director_dao.values())
    director_dao.create = MagicMock(return_value=data_for_director_dao.get(1))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()
    return director_dao


@pytest.fixture
def data_for_genre_dao():
    genre_1 = Genre(id=1, name='name_1')
    genre_2 = Genre(id=2, name='name_2')
    genre_3 = Genre(id=3, name='name_3')
    genre_4 = Genre(id=4, name='name_4')
    return {1: genre_1, 2: genre_2, 3: genre_3, 4: genre_4}


@pytest.fixture
def genre_dao(data_for_genre_dao):
    genre_dao = GenreDAO(None)
    genre_dao.get_one = MagicMock(side_effect=data_for_genre_dao.get)
    genre_dao.get_all = MagicMock(return_value=data_for_genre_dao.values())
    genre_dao.create = MagicMock(return_value=data_for_genre_dao.get(1))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()
    return genre_dao


@pytest.fixture
def data_for_movie_dao():
    movie_1 = Movie(id=1, title=1, description=1, trailer=1, year=1, rating=1, genre_id=1, genre=1, director_id=1,
                    director=1)
    movie_2 = Movie(id=2, title=2, description=2, trailer=2, year=2, rating=2, genre_id=2, genre=2, director_id=2,
                    director=2)
    movie_3 = Movie(id=3, title=3, description=3, trailer=3, year=3, rating=3, genre_id=3, genre=3, director_id=3,
                    director=3)
    movie_4 = Movie(id=4, title=4, description=4, trailer=4, year=4, rating=4, genre_id=4, genre=4, director_id=4,
                    director=4)
    return {1: movie_1, 2: movie_2, 3: movie_3, 4: movie_4}


@pytest.fixture
def movie_dao(data_for_movie_dao):
    movie_dao = MovieDAO(None)
    movie_dao.get_one = MagicMock(side_effect=data_for_movie_dao.get)
    movie_dao.get_all = MagicMock(return_value=data_for_movie_dao.values())
    movie_dao.create = MagicMock(return_value=data_for_movie_dao.get(1))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()
    return movie_dao

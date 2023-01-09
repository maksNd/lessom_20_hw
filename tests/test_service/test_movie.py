import pytest
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        assert self.movie_service.get_one(1) is not None
        assert self.movie_service.get_one(1).title == 1

    def test_get_all(self):
        assert self.movie_service.get_all() is not None
        assert len(self.movie_service.get_all()) > 0

    def test_create(self):
        data = {'id': 1, 'title': 'name_1'}
        assert self.movie_service.create(data) is not None
        assert self.movie_service.create(data).title == 1

    def test_update(self):
        data = {'name': 'name_1'}
        assert self.movie_service.update(data) is not None

    def test_delete(self):
        assert self.movie_service.delete(1) is None

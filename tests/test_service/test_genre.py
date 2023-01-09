import pytest
from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        assert self.genre_service.get_one(1) is not None
        assert self.genre_service.get_one(1).name == 'name_1'

    def test_get_all(self):
        assert self.genre_service.get_all() is not None
        assert len(self.genre_service.get_all()) > 0

    def test_create(self):
        data = {'id': 1, 'name': 'name_1'}
        assert self.genre_service.create(data) is not None
        assert self.genre_service.create(data).name == 'name_1'

    def test_update(self):
        data = {'name': 'name_1'}
        assert self.genre_service.update(data) is not None

    def test_delete(self):
        assert self.genre_service.delete(1) is None

import pytest
from service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        assert self.director_service.get_one(1) is not None
        assert self.director_service.get_one(1).name == 'name_1'

    def test_get_all(self):
        assert self.director_service.get_all() is not None
        assert len(self.director_service.get_all()) > 0

    def test_create(self):
        data = {'id': 1, 'name': 'name_1'}
        assert self.director_service.create(data) is not None
        assert self.director_service.create(data).name == 'name_1'

    def test_update(self):
        data = {'name': 'name_1'}
        assert self.director_service.update(data) is not None

    def test_delete(self):
        assert self.director_service.delete(1) is None

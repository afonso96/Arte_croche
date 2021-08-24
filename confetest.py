import pytest

from products.test.factorys import CategoryFactory, ProductFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def category():
    return CategoryFactory()


@pytest.fixture
def product():
    return ProductFactory()

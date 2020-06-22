import os
import pytest
import config

from config.settings.base import BASE_DIR

from django.test import RequestFactory
from backend.users.models import User
from backend.users.tests.factories import UserFactory

@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()

# tells pytest to conntect the existing sqlitedb instead of postgres
@pytest.fixture(scope='session')
def django_db_setup():
    config.settings.base.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

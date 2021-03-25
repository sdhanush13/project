import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  assert User.objects.count() == 1


def test_greater_equal():
  num = 100
  assert num > 10

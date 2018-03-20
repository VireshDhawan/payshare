import pytest
from model_mommy import mommy
from rest_framework import status


@pytest.fixture
def collective(db):
    collective = mommy.make("purchases.Collective")
    return collective


def test_collective(collective, client):
    url = "/api/v1/{}".format(collective.key)
    response = client.get(url, follow=True)
    assert response.status == status.HTTP_200_OK

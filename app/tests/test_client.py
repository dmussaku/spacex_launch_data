import pytest

from app.src.client import SpaceXClient


def test_get_launches(launches_data):
    cli = SpaceXClient()
    data = cli.get_launches()
    assert data == launches_data
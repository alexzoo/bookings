import pytest


@pytest.mark.smoke
def test_can_health_check(ping):
    ping.health_check()

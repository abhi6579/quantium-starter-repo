import pytest

@pytest.fixture
def dash_duo(dash_duo):
    """Configure dash_duo fixture with longer timeout"""
    dash_duo.driver.implicitly_wait(10)
    return dash_duo

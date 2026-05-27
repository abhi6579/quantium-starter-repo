import pytest
from dash.testing.application_runners import import_app
import dash

# Test 1: Header is present
def test_header_present(dash_duo):
    """Test that the header/title is present in the app"""
    # Import your app from app.py
    app = import_app('app')
    dash_duo.start_server(app)
    
    # Find the header element (h1 tag)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsels" in header.text

# Test 2: Visualisation is present
def test_visualisation_present(dash_duo):
    """Test that the chart/graph is present in the app"""
    app = import_app('app')
    dash_duo.start_server(app)
    
    # Find the graph element
    graph = dash_duo.find_element(".dash-graph")
    assert graph is not None
    assert graph.is_displayed()

# Test 3: Region picker is present
def test_region_picker_present(dash_duo):
    """Test that the region picker radio buttons are present"""
    app = import_app('app')
    dash_duo.start_server(app)
    
    # Find any radio button input
    radio_buttons = dash_duo.find_elements("input[type='radio']")
    assert len(radio_buttons) > 0
    
    # Check for region text in the page
    body_text = dash_duo.find_element("body").text.lower()
    has_regions = any(region in body_text for region in ["north", "east", "south", "west", "all"])
    assert has_regions

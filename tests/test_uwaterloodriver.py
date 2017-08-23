from pytest import fixture
import vcr
from uwaterloodriver import UW_Driver

@fixture
def foodservices_menu_keys():
    # Responsible for only returning the test data
    return ['date', 'outlets']

@fixture
def date_keys():
    return ['year', 'week', 'start', 'end']

@fixture
def outlets_keys():
    return ['outlet_name', 'outlet_id', "menu"]

@fixture
def menu_keys():
    return ['date', 'day', 'meals', 'notes']

@fixture
def meals_keys():
    return ['lunch', 'dinner']

@fixture
def notes_keys():
    return ['date', 'outlet_name', 'outlet_id', 'note']


@vcr.use_cassette('vcr_cassettes/foodservices_menu.yml', filter_query_parameters=['key'])
def test_foodservices_menu(foodservices_menu_keys, date_keys):
    """Tests an API call to /foodservices/menu/ endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_menu()

    assert isinstance(response, dict)
    # Not testing subkeys in 'outlets' because it could be empty at certain times.
    assert set(foodservices_menu_keys).issubset(response.keys()), "All keys should be in the response."
    assert set(date_keys).issubset(response['date'].keys()), "All date keys should be present."
    assert isinstance(response['outlets'], list)


@vcr.use_cassette('vcr_cassettes/foodservices_year_week_menu.yml', filter_query_parameters=['key'])
def test_foodservices_year_week_menu(foodservices_menu_keys, date_keys, outlets_keys, menu_keys, meals_keys):
    """Tests an API call to /foodservices/{year}/{week}/menu endpoint.
        year = 2017, week = 20"""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_menu(2017, 20)

    assert isinstance(response, dict)
    assert isinstance(response['outlets'], list)
    assert set(date_keys).issubset(response['date'].keys()), "All date keys should be present."
    assert set(foodservices_menu_keys).issubset(response.keys()), "All keys should be in the response."
    assert set(outlets_keys).issubset(response['outlets'][0].keys()), "All outlets keys should be present."
    assert set(menu_keys).issubset(response['outlets'][0]['menu'][0].keys()), "All menu keys should be present."
    assert set(meals_keys).issubset(response['outlets'][0]['menu'][0]['meals'].keys()), "All meal keys should be present."


@vcr.use_cassette('vcr_cassettes/foodservices_notes.yml', filter_query_parameters=['key'])
def test_foodservices_notes():
    """Tests an API call to /foodservices/notes/ endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_notes()

    assert isinstance(response, list)


@vcr.use_cassette('vcr_cassettes/foodservices_year_week_notes.yml', filter_query_parameters=['key'])
def test_foodservices_year_week_notes(notes_keys):
    """Tests an API call to /foodservices/{year}/{week}/notes endpoint.
        year = 2017, week = 15"""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_notes(2017, 15)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(notes_keys).issubset(response[0].keys()), "All notes keys should be present."


from pytest import fixture
import vcr
from uwaterloodriver import UW_Driver

@fixture
def menu_keys():
    # Responsible for only returning the test data
    return ['date', 'outlets']

@fixture
def date_keys():
    return ['year', 'week', 'start', 'end']

@vcr.use_cassette('vcr_cassettes/foodservices_menu.yml', filter_query_parameters=['key'])
def test_foodservices_manu(menu_keys, date_keys):
    """Tests an API call to /foodservices/menu/ endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_menu()

    assert isinstance(response, dict)
    # Not testing subkeys in 'outlets' because it could be empty at certain times.
    assert set(menu_keys).issubset(response.keys()), "All keys should be in the response."
    assert set(date_keys).issubset(response['date'].keys()), "All date keys should be present."
    assert isinstance(response['outlets'], list)

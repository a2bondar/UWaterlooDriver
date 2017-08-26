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

@fixture
def announce_keys():
    return ['date', 'ad_text']

@fixture
def foodservices_outlets_keys():
    return ['outlet_id', 'outlet_name', 'has_breakfast', 'has_lunch', 'has_dinner']

@fixture
def diets_keys():
    return ['diet_id', 'diet_type']

@fixture
def locations_keys():
    return ['outlet_id', 'outlet_name', 'building', 'logo', 'latitude',
            'longitude', 'description', 'notice', 'is_open_now',
            'opening_hours', 'special_hours', 'dates_closed']

@fixture
def watcard_keys():
    return ['vendor_id', 'vendor_name']

# product_keys() does not exhaustively test all return keys (unnecessary)
@fixture
def products_keys():
    return ['product_id', 'product_name', 'ingredients', 'serving_size',
            'serving_size_ml', 'serving_size_g', 'calories', 'total_fat_g',
            'total_fat_percent', 'fat_saturated_g', 'fat_saturated_percent',
            'fat_trans_g', 'fat_trans_percent']


@vcr.use_cassette('vcr_cassettes/foodservices/foodservices_menu.yml', filter_query_parameters=['key'])
def test_foodservices_menu(foodservices_menu_keys, date_keys):
    """Tests an API call to /foodservices/menu/ endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_menu()

    assert isinstance(response, dict)
    # Not testing subkeys in 'outlets' because it could be empty at certain times.
    assert set(foodservices_menu_keys).issubset(response.keys()), "All keys should be in the response."
    assert set(date_keys).issubset(response['date'].keys()), "All date keys should be present."
    assert isinstance(response['outlets'], list)


@vcr.use_cassette('vcr_cassettes/foodservices/foodservices_year_week_menu.yml', filter_query_parameters=['key'])
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


@vcr.use_cassette('vcr_cassettes/foodservices/foodservices_notes.yml', filter_query_parameters=['key'])
def test_foodservices_notes():
    """Tests an API call to /foodservices/notes/ endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_notes()

    assert isinstance(response, list)


@vcr.use_cassette('vcr_cassettes/foodservices/foodservices_year_week_notes.yml', filter_query_parameters=['key'])
def test_foodservices_year_week_notes(notes_keys):
    """Tests an API call to /foodservices/{year}/{week}/notes endpoint.
        year = 2017, week = 15"""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_notes(2017, 15)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(notes_keys).issubset(response[0].keys()), "All notes keys should be present."


@vcr.use_cassette('vcr_cassettes/foodservices/foodservices_announcements.yml', filter_query_parameters=['key'])
def test_foodservices_announcements():
    """Tests an API call to /foodservices/announcements/ endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_announcements()

    assert isinstance(response, list)


@vcr.use_cassette('vcr_cassettes/foodservices/foodservices_year_week_announcements.yml', filter_query_parameters=['key'])
def test_foodservices_year_week_announcements(announce_keys):
    """Tests an API call to /foodservices/{year}/{week}/announcements endpoint.
        year = 2016, week = 16"""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_announcements(2016, 16)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(announce_keys).issubset(response[0].keys()), "All notes keys should be present."


@vcr.use_cassette('vcr_cassettes/foodservices/foodservices_outlets.yml', filter_query_parameters=['key'])
def test_foodservices_outlets(foodservices_outlets_keys):
    """Tests an API call to /foodservices/outlets endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_outlets()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(foodservices_outlets_keys).issubset(response[0].keys()), "All outlets keys should be present."


@vcr.use_cassette('vcr_cassettes/foodservices/foodservices_diets.yml', filter_query_parameters=['key'])
def test_foodservices_diets(diets_keys):
    """Tests an API call to /foodservices/diets endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_diets()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(diets_keys).issubset(response[0].keys()), "All outlets keys should be present."


@vcr.use_cassette('vcr_cassettes/foodservices/foodservices_locations.yml', filter_query_parameters=['key'])
def test_foodservices_locations(locations_keys):
    """Tests an API call to /foodservices/locations endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_locations()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(locations_keys).issubset(response[0].keys()), "All locations keys should be present."


@vcr.use_cassette('vcr_cassettes/foodservices/foodservices_watcard.yml', filter_query_parameters=['key'])
def test_foodservices_watcard(watcard_keys):
    """Tests an API call to /foodservices/watcard endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_watcard()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(watcard_keys).issubset(response[0].keys()), "All watcard keys should be present."

@vcr.use_cassette('vcr_cassettes/foodservices/foodservices_products.yml', filter_query_parameters=['key'])
def test_foodservices_products(products_keys):
    """Tests an API call to /foodservices/products/{product_id} endpoint.
        product_id = 1386"""

    uw_driver = UW_Driver()
    response = uw_driver.foodservices_products(1386)

    assert isinstance(response, dict)
    assert response['product_id'] == 1386, "The ID should be in the response."
    assert set(products_keys).issubset(response.keys()), "All product keys should be present."

from pytest import fixture
import vcr
from uwaterloodriver import UW_Driver

@fixture
def feds_events_keys():
    # Responsible for only returning the test data
    return ['id', 'title', 'location', 'start', 'end', 'categories',
            'url', 'updated']

@fixture
def events_keys():
    return ['id', 'title', 'location', 'description', 'description_raw',
            'start', 'end', 'categories', 'url', 'updated']

@fixture
def locations_keys():
    return ['outlet_id', 'outlet_name', 'building', 'logo', 'latitude',
            'longitude', 'description', 'notice', 'is_open_now',
            'opening_hours', 'special_hours', 'dates_closed']


@vcr.use_cassette('vcr_cassettes/feds/feds_events.yml', filter_query_parameters=['key'])
def test_feds_events(feds_events_keys):
    """Tests an API call to /feds/events endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.feds_events()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(feds_events_keys).issubset(response[0].keys()), "All events keys should be present."


@vcr.use_cassette('vcr_cassettes/feds/feds_events_eventid.yml', filter_query_parameters=['key'])
def test_feds_event_id(events_keys):
    """Tests an API call to /feds/events/{event_id} endpoint.
        product_id = 300787"""

    uw_driver = UW_Driver()
    response = uw_driver.feds_events(300787)

    assert isinstance(response, dict)
    assert response['id'] == 300787, "The ID should be in the response."
    assert set(events_keys).issubset(response.keys()), "All product keys should be present."


@vcr.use_cassette('vcr_cassettes/feds/feds_locations.yml', filter_query_parameters=['key'])
def test_feds_locations(locations_keys):
    """Tests an API call to /feds/locations endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.feds_locations()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(locations_keys).issubset(response[0].keys()), "All locations keys should be present."


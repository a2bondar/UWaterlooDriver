from pytest import fixture
import vcr
from uwaterloodriver import UW_Driver

@fixture
def list_keys():
    # Responsible for only returning the test data
    return ['current_term', 'previous_term', 'next_term', 'listings']

@fixture
def courses_keys():
    return ['units', 'catalog_number', 'subject', 'title']

@fixture
def examschedule_keys():
    return ['course', 'sections']

@fixture
def examschedule_sections_keys():
    return ['section', 'day', 'date', 'start_time', 'end_time', 'location', 'notes']

@fixture
def schedule_keys():
    return ['subject', 'catalog_number', 'units', 'title', 'note', 'class_number', 'section',
            'campus', 'associated_class', 'related_component_1', 'related_component_2',
            'enrollment_capacity', 'enrollment_total', 'waiting_capacity', 'waiting_total',
            'topic', 'reserves', 'classes', 'held_with', 'term', 'academic_level', 'last_updated']

@fixture
def enrollment_keys():
    return ['subject', 'catalog_number', 'class_number', 'section', 'enrollment_capacity',
            'enrollment_total', 'waiting_capacity', 'waiting_total', 'last_updated']

@fixture
def importantdates_keys():
    return ['id', 'title', 'body', 'body_raw', 'special_notes', 'special_notes_raw', 'audience',
            'term', 'term_id', 'start_date', 'end_date', 'date_tbd', 'date_na', 'link',
            'site', 'vid', 'updated']

@fixture
def infosessions_keys():
    return ['id', 'employer', 'date', 'start_time', 'end_time', 'description', 'website',
            'building', 'audience', 'link']


@vcr.use_cassette('vcr_cassettes/terms/terms_list.yml', filter_query_parameters=['key'])
def test_terms_list(list_keys):
    """Tests an API call to /terms/list endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.terms_list()

    assert isinstance(response, dict)
    assert set(list_keys).issubset(response.keys()), "All terms_list keys should be present."


@vcr.use_cassette('vcr_cassettes/terms/terms_courses.yml', filter_query_parameters=['key'])
def test_terms_courses(courses_keys):
    """Tests an API call to /terms/{term_id}/courses endpoint.
        term_id = 1161"""

    uw_driver = UW_Driver()
    response = uw_driver.terms_courses(1161)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(courses_keys).issubset(response[0].keys()), "All terms_courses keys should be present."


@vcr.use_cassette('vcr_cassettes/terms/terms_examschedule.yml', filter_query_parameters=['key'])
def test_terms_examschedule(examschedule_keys, examschedule_sections_keys):
    """Tests an API call to /terms/{term}/examschedule endpoint.
        term_id = 1139"""

    uw_driver = UW_Driver()
    response = uw_driver.terms_examschedule(1139)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(examschedule_keys).issubset(response[0].keys()), "All terms_examschedule keys should be present."
    assert set(examschedule_sections_keys).issubset(response[0]["sections"][0].keys()), "All terms_examschedule_sections keys should be present."


@vcr.use_cassette('vcr_cassettes/terms/terms_schedule.yml', filter_query_parameters=['key'])
def test_terms_schedule(schedule_keys):
    """Tests an API call to /terms/{term}/{subject}/schedule endpoint.
        term_id = 1139, subject = MATH"""

    uw_driver = UW_Driver()
    response = uw_driver.terms_schedule(term_id=1139, subject="MATH")

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(schedule_keys).issubset(response[0].keys()), "All terms_schedule keys should be present."


@vcr.use_cassette('vcr_cassettes/terms/terms_schedule_with_catalog.yml', filter_query_parameters=['key'])
def test_terms_schedule_catalog(schedule_keys):
    """Tests an API call to /terms/{term}/{subject}/{catalog_number}/schedule endpoint.
        term_id = 1139, subject = CS, catalog_number = 115"""

    uw_driver = UW_Driver()
    response = uw_driver.terms_schedule(term_id=1139, subject="MATH", catalog_number=115)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(schedule_keys).issubset(response[0].keys()), "All terms_schedule keys should be present."


@vcr.use_cassette('vcr_cassettes/terms/terms_enrollment.yml', filter_query_parameters=['key'])
def test_terms_enrollment(enrollment_keys):
    """Tests an API call to /terms/{term}/enrollment endpoint.
        term_id = 1159"""

    uw_driver = UW_Driver()
    response = uw_driver.terms_enrollment(1159)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(enrollment_keys).issubset(response[0].keys()), "All terms_enrollment keys should be present."


@vcr.use_cassette('vcr_cassettes/terms/terms_enrollment_with_subject.yml', filter_query_parameters=['key'])
def test_terms_enrollment_subject(enrollment_keys):
    """Tests an API call to /terms/{term}/{seubject}/enrollment endpoint.
        term_id = 1159, subject = ITAL"""

    uw_driver = UW_Driver()
    response = uw_driver.terms_enrollment(1159, subject="ITAL")

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(enrollment_keys).issubset(response[0].keys()), "All terms_enrollment keys should be present."


@vcr.use_cassette('vcr_cassettes/terms/terms_importantdates.yml', filter_query_parameters=['key'])
def test_terms_importantdates(importantdates_keys):
    """Tests an API call to /terms/{term}/importantdates endpoint.
        term_id = 1179"""

    uw_driver = UW_Driver()
    response = uw_driver.terms_importantdates(1179)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(importantdates_keys).issubset(response[0].keys()), "All terms_importantdates keys should be present."


@vcr.use_cassette('vcr_cassettes/terms/terms_infosessions.yml', filter_query_parameters=['key'])
def test_terms_infosessions(infosessions_keys):
    """Tests an API call to /terms/{term}/infosessions endpoint.
        term_id = 1141"""

    uw_driver = UW_Driver()
    response = uw_driver.terms_infosessions(1141)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(infosessions_keys).issubset(response[0].keys()), "All terms_infosessions keys should be present."

from pytest import fixture
import vcr
from uwaterloodriver import UW_Driver

"""Below are a list of key fixtures to test responses with, they are NOT exhaustive."""
@fixture
def courses_keys():
    # Responsible for only returning the test data
    return ['course_id', 'subject', 'catalog_number', 'title']

@fixture
def subject_keys():
    return ['units', 'description', 'academic_level']

@fixture
def course_id_keys():
    return ['instructions', 'prerequisites', 'antirequisites', 'crosslistings',
            'terms_offered', 'notes']

@fixture
def schedule_keys():
    return ['title', 'class_number', 'section', 'campus', 'associated_class']

@fixture
def prereq_keys():
    return ['subject', 'catalog_number', 'title', 'prerequisites', 'prerequisites_parsed']

@fixture
def examschedule_keys():
    return ['course', 'sections']

@vcr.use_cassette('vcr_cassettes/courses/courses.yml', filter_query_parameters=['key'])
def test_courses(courses_keys):
    """Tests an API call to /courses/ endpoint."""

    uw_driver = UW_Driver()
    response = uw_driver.courses()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(courses_keys).issubset(response[0].keys()), "All courses keys should be present."


@vcr.use_cassette('vcr_cassettes/courses/courses_subjects.yml', filter_query_parameters=['key'])
def test_courses_subjects(courses_keys, subject_keys):
    """Tests an API call to /courses/{subject} endpoint.
        subject=MATH"""

    uw_driver = UW_Driver()
    response = uw_driver.courses(subject="MATH")

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(courses_keys).issubset(response[0].keys()), "All courses keys should be present."
    assert set(subject_keys).issubset(response[0].keys()), "All subjects keys should be present."


@vcr.use_cassette('vcr_cassettes/courses/courses_course_id.yml', filter_query_parameters=['key'])
def test_courses(courses_keys, subject_keys, course_id_keys):
    """Tests an API call to /courses/{course_id} endpoint.
        course_id=007407"""

    uw_driver = UW_Driver()
    response = uw_driver.courses(course_id=7407)

    assert isinstance(response, dict)
    assert set(courses_keys).issubset(response.keys())
    assert set(subject_keys).issubset(response.keys())
    assert set(course_id_keys).issubset(response.keys())


@vcr.use_cassette('vcr_cassettes/courses/courses_schedule_course_num.yml', filter_query_parameters=['key'])
def test_courses_schedule_by_class_number(schedule_keys):
    """Tests an API call to /courses/{class_number}/schedule endpoint.
        class_number=5377"""

    uw_driver = UW_Driver()
    response = uw_driver.courses_schedule(class_num=5377)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(schedule_keys).issubset(response[0].keys())


@vcr.use_cassette('vcr_cassettes/courses/courses_by_subject_catalog.yml', filter_query_parameters=['key'])
def test_courses_by_subject_catalog(courses_keys, course_id_keys):
    """Tests an API call to /courses/{subject}/{catalog_number} endpoint.
        subject=PHYS, catalog=234"""

    uw_driver = UW_Driver()
    response = uw_driver.courses(subject="PHYS", catalog_num=234)

    assert isinstance(response, dict)
    assert set(courses_keys).issubset(response.keys())
    assert set(course_id_keys).issubset(response.keys())


@vcr.use_cassette('vcr_cassettes/courses/courses_schedule_by_subject_catalog.yml', filter_query_parameters=['key'])
def test_courses_schedule_by_subject_catalog(schedule_keys):
    """Tests an API call to /courses/{subject}/{catalog_number}/schedule endpoint.
        subject=CS, catalog=486"""

    uw_driver = UW_Driver()
    response = uw_driver.courses_schedule(subject="CS", catalog_num=486)

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(schedule_keys).issubset(response[0].keys())


@vcr.use_cassette('vcr_cassettes/courses/courses_prerequisites.yml', filter_query_parameters=['key'])
def test_courses_prerequisites(prereq_keys):
    """Tests an API call to /courses/{subject}/{catalog_number}/prerequisites endpoint.
        subject=PHYS, catalog=375"""

    uw_driver = UW_Driver()
    response = uw_driver.courses_prerequisites("PHYS", 375)

    assert isinstance(response, dict)
    assert set(prereq_keys).issubset(response.keys())


@vcr.use_cassette('vcr_cassettes/courses/courses_examschedule.yml', filter_query_parameters=['key'])
def test_courses_examschedule(examschedule_keys):
    """Tests an API call to /courses/{subject}/{catalog_number}/examschedule endpoint.
        subject=CS, catalog=486"""

    uw_driver = UW_Driver()
    response = uw_driver.courses_examschedule("CS", 486)

    assert isinstance(response, dict)
    assert set(examschedule_keys).issubset(response.keys())

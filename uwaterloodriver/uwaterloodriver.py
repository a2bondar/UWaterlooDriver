from . import session

# Exception for inccorect number or invalid parameters passed to endpoint.
class InvalidParameters(Exception):
    pass


class UW_Driver(object):

    def __init__(self, base_url='https://api.uwaterloo.ca/v2'):
        self.base_url = base_url

    def __get_data(self, *args):
        endpoint = self.__update_url(args)
        response = session.get("{}{}.{}".format(self.base_url, endpoint, "json"))
        json_data = response.json()
        return json_data["data"]

    def __update_url(self, *args):
        endpoint = ""
        for arg in args:
            if (arg is None or arg == ""):
                continue
            endpoint = "{}/{}".format(endpoint, arg)
        return endpoint

    def __foodservices_get(self, suffix, year=None, week=None):
        prefix = "foodservices"
        if ((year is None and week is None) or
            (year is not None and week is not None)):
            return self.__get_data(prefix, year, week, suffix)
        else:
            raise InvalidParameters(
                "ERROR: {}/year/week/{} endpoint "
                "expects two integer values (year, week) or None.".format(prefix, suffix)
            )

    ### Food Services ###

    def foodservices_menu(self, year=None, week=None):
        suffix = "menu"
        return self.__foodservices_get(suffix, year, week)

    def foodservices_notes(self, year=None, week=None):
        suffix = "notes"
        return self.__foodservices_get(suffix, year, week)

    def foodservices_announcements(self, year=None, week=None):
        suffix = "announcements"
        return self.__foodservices_get(suffix, year, week)

    def foodservices_diets(self):
        suffix = "diets"
        return self.__foodservices_get(suffix)

    def foodservices_outlets(self):
        suffix = "outlets"
        return self.__foodservices_get(suffix)

    def foodservices_locations(self):
        suffix = "locations"
        return self.__foodservices_get(suffix)

    def foodservices_watcard(self):
        suffix = "watcard"
        return self.__foodservices_get(suffix)

    def foodservices_products(self, product_id):
        suffix = "products/{}".format(product_id)
        return self.__foodservices_get(suffix)

    ### FEDS ###

    def feds_events(self, event_id=""):
        prefix = "feds"
        suffix = "events"
        return self.__get_data(prefix, suffix, event_id)

    def feds_locations(self):
        prefix = "feds"
        suffix = "locations"
        return self.__get_data(prefix, suffix)

    ### Course ###

    def courses(self, subject=None, catalog_num=None, course_id=None):
        prefix = "courses"
        if (subject is None and catalog_num is None and course_id is None):
            # endpoint: /courses
            return self.__get_data(prefix)
        elif (subject is not None and catalog_num is None and course_id is None):
            # endpoint: /courses/{subject}
            return self.__get_data(prefix, subject)
        elif (subject is not None and catalog_num is not None and course_id is None):
            # endpoint: /courses/{subject}/{catalog_num}
            return self.__get_data(prefix, subject, catalog_num)
        elif (subject is None and catalog_num is None and course_id is not None):
            # endpoint: /courses/{course_id}
            return self.__get_data(prefix, course_id)
        else:
            raise InvalidParameters(
                "ERROR: /courses/... endpoint [courses()]"
                "accepts only the following parameters: \n"
                "/courses/"
                "/courses/{subject}"
                "/courses/{course_id}"
                "courses/{subject}/{catalog_num}"
            )

    def courses_schedule(self, class_num=None, subject=None, catalog_num=None):
        """Schedule for /courses/ endpoint. Either class_num is None or subject
            and catalog_num is None. Not both, or neither."""
        prefix = "courses"
        suffix = "schedule"
        if ((class_num is not None) and
            (subject is None and catalog_num is None)):
            return self.__get_data(prefix, class_num, suffix)
        elif ((class_num is None) and
              (subject is not None and catalog_num is not None)):
            return self.__get_data(prefix, subject, catalog_num, suffix)
        else:
            raise InvalidParameters(
                "ERROR: /courses/.../schedule endpoint "
                "expects either a class_number or a "
                "subject and catalog_number pair but NOT BOTH."
            )

    def courses_prerequisites(self, subject, catalog_num):
        prefix = "courses"
        suffix = "prerequisites"
        return self.__get_data(prefix, subject, catalog_num, suffix)

    def courses_examschedule(self, subject, catalog_num):
        prefix = "courses"
        suffix = "examschedule"
        return self.__get_data(prefix, subject, catalog_num, suffix)

    ### Awards ###

    def awards_graduate(self):
        prefix = "awards"
        suffix = "graduate"
        return self.__get_data(prefix, suffix)

    def awards_undergraduate(self):
        prefix = "awards"
        suffix = "undergraduate"
        return self.__get_data(prefix, suffix)

    ### Events ###

    def events(self, site="", id=""):
        prefix = "events"
        return self.__get_data(prefix, site, id)

    def events_holidays(self):
        prefix = "events"
        suffix = "holidays"
        return self.__get_data(prefix, suffix)

    ### News ###

    def news(self, site="", id=""):
        prefix = "news"
        return self.__get_data(prefix, site, id)

    ### Opportunities ###

    def opportunities(self, site="", id=""):
        prefix = "opportunities"
        return self.__get_data(prefix, site, id)

    ### Services ###

    def services(self, site):
        prefix = "services"
        return self.__get_data(prefix, site)

    ### Weather ###

    def weather(self):
        prefix = "weather"
        suffix = "current"
        return self.__get_data(prefix, suffix)

    ### Terms ###

    def terms_list(self):
        prefix = "terms"
        suffix = "list"
        return self.__get_data(prefix, suffix)

    def terms_courses(self, term):
        prefix = "terms"
        suffix = "courses"
        return self.__get_data(prefix, term, suffix)

    def terms_examschedule(self, term):
        prefix = "terms"
        suffix = "examschedule"
        return self.__get_data(prefix, term, suffix)

    def terms_schedule(self, term, subject, catalog_number=None):
        prefix = "terms"
        suffix = "schedule"
        return self.__get_data(prefix, term, subject, catalog_number, suffix)

    def terms_enrollment(self, term, subject=None):
        prefix = "terms"
        suffix = "enrollment"
        return self.__get_data(prefix, term, subject, suffix)

    def terms_importantdates(self, term):
        prefix = "terms"
        suffix = "importantdates"
        return self.__get_data(prefix, term, suffix)

    def terms_infosessions(self, term):
        prefix = "terms"
        suffix = "infosessions"
        return self.__get_data(prefix, term, suffix)

    ### Resources ###

    def resources_tutors(self):
        prefix = "resources"
        suffix = "tutors"
        return self.__get_data(prefix, suffix)

    def resources_infosessions(self):
        prefix = "resources"
        suffix = "infosessions"
        return self.__get_data(prefix, suffix)

    def resources_goosewatch(self):
        prefix = "resources"
        suffix = "goosewatch"
        return self.__get_data(prefix, suffix)

    def resources_sunshinelist(self):
        prefix = "resources"
        suffix = "sunshinelist"
        return self.__get_data(prefix, suffix)

    ### Definitions and Codes

    def codes_units(self):
        prefix = "codes"
        suffix = "units"
        return self.__get_data(prefix, suffix)

    def codes_terms(self):
        prefix = "codes"
        suffix = "terms"
        return self.__get_data(prefix, suffix)

    def codes_groups(self):
        prefix = "codes"
        suffix = "groups"
        return self.__get_data(prefix, suffix)

    def codes_subjects(self):
        prefix = "codes"
        suffix = "subjects"
        return self.__get_data(prefix, suffix)

    def codes_instructions(self):
        prefix = "codes"
        suffix = "intructions"
        return self.__get_data(prefix, suffix)

    ### Building ###

    def buildings_list(self):
        prefix = "buildings"
        suffix = "list"
        return self.__get_data(prefix, suffix)

    def buildings(self, building_code):
        prefix = "buildings"
        return self.__get_data(prefix, building_code)

    def buildings_courses(self, building_code, room):
        prefix = "buildings"
        suffix = "courses"
        return self.__get_data(prefix, building_code, room, suffix)

    def buildings_accesspoints(self, building_code):
        prefix = "buildings"
        suffix = "accesspoints"
        return self.__get_data(prefix, building_code, suffix)

    def buildings_vendingmachines(self, building_code):
        prefix = "buildings"
        suffix = "vendingmachines"
        return self.__get_data(prefix, building_code, suffix)

    

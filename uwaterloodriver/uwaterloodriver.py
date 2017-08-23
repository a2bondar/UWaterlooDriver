from . import session

# Exception for inccorect number or invalid parameters passed to endpoint.
class InvalidParameters(Exception):
    pass


class UW_Driver(object):

    def __init__(self, base_url='https://api.uwaterloo.ca/v2'):
        self.base_url = base_url

    def __get_data(self, endpoint):
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
            endpoint = self.__update_url(prefix, year, week, suffix)
            return self.__get_data(endpoint)
        else:
            raise InvalidParameters(
                "ERROR: {}/year/week/{} endpoint "
                "expects two integer values (year, week) or None.".format(prefix, suffix)
            )

    def __feds_get(self, suffix, event_id=None):
        prefix = "feds"
        endpoint = self.__update_url(prefix, suffix, event_id)
        return self.__get_data(endpoint)

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

    def feds_events(self, event_id=None):
        suffix = "events"
        return self.__feds_get(suffix, event_id)

    def feds_locations(self):
        suffix = "locations"
        return self.__feds_get(suffix)


    ### Awards ###

    def awards_graduate(self):
        endpoint = "/awards/graduate"
        return self.__get_data(endpoint)

    def awards_undergraduate(self):
        endpoint = "/awards/undergraduate"
        return self.__get_data(endpoint)
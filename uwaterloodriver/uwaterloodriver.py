from . import session


class UW_Driver(object):

    def __init__(self, base_url='https://api.uwaterloo.ca/v2/'):
        self.base_url = base_url

    def __get_data(self, endpoint):
        response = session.get("{}{}.{}".format(self.base_url, endpoint, "json"))
        json_data = response.json()
        return json_data["data"]

    # Food Services
    def foodservices_menu(self):
        endpoint = "foodservices/menu"
        return self.__get_data(endpoint)

    # Awards

    def awards_graduate(self):
        endpoint = "awards/graduate"
        return self.__get_data(endpoint)

    def awards_undergraduate(self):
        endpoint = "awards/undergraduate"
        return self.__get_data(endpoint)
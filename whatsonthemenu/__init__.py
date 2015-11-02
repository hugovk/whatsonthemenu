#!/usr/bin/env python
# encoding: utf-8
"""
Python interface for NYPL's What's on The Menu API
https://github.com/NYPL/menus-api
"""
from __future__ import print_function, unicode_literals
import requests

__version__ = '0.1.0'


class WhatsOnTheMenu(object):
    """ Python interface for NYPL's What's on The Menu API """
    def __init__(self, token):
        self.token = token
        self.base_url = "http://api.menus.nypl.org/"
        self.ratelimit_limit = None
        self.ratelimit_remaining = None

    def nypl_menus_api(self, method, params=None):
        """ Call the API and return JSON """
        if not params:
            params = ""
        url = self.base_url + method + "?token=" + self.token + params
        r = requests.get(url)

        self.ratelimit_limit = r.headers['X-Ratelimit-Limit']
        self.ratelimit_remaining = r.headers['X-Ratelimit-Remaining']

        if (r.status_code) == 200:
            return r.json()

        return None

    def _paramify(self, params, param_name, param_value):
        """ If param_value, append &param_name=param_value to params """
        if param_value:
            params += "&" + param_name + "=" + str(param_value)
        return params

    def _paramify_pages(self, per_page, page):
        """ Initialise params string with per_page and page """
        params = ""
        params = self._paramify(params, "per_page", per_page)
        params = self._paramify(params, "page", page)
        return params

    def rate_limit(self):
        """
        Return the daily rate limit, and how many your API token has remaining
        """
        if not self.ratelimit_limit or not self.ratelimit_remaining:
            # Not cached so make a dummy call to fetch them
            self.get_menus(min_year=9999)
        return self.ratelimit_limit, self.ratelimit_remaining

    def rate_limit_remaining(self):
        """
        Return how many calls your API token has remaining today
        """
        _, remaining = self.rate_limit()
        return remaining

    def get_menus(self, per_page=None, page=None, min_year=None, max_year=None,
                  sort_by=None, status=None):
        """ GET /menus """
        params = self._paramify_pages(per_page, page)
        params = self._paramify(params, "min_year", min_year)
        params = self._paramify(params, "max_year", max_year)
        params = self._paramify(params, "sort_by", sort_by)
        params = self._paramify(params, "status", status)

        method = "menus"
        return self.nypl_menus_api(method, params)

    def get_menus_id(self, id, per_page=None, page=None):
        """ GET /menus/{id} """
        params = self._paramify_pages(per_page, page)

        method = "menus/" + str(id)
        return self.nypl_menus_api(method, params)

    def get_menus_id_pages(self, id, per_page=None, page=None):
        """ GET /menus/{id}/pages """
        params = self._paramify_pages(per_page, page)

        method = "menus/" + str(id) + "/pages"
        return self.nypl_menus_api(method, params)

    def get_menus_id_dishes(self, id, per_page=None, page=None):
        """ GET /menus/{id}/dishes """
        params = self._paramify_pages(per_page, page)

        method = "menus/" + str(id) + "/dishes"
        return self.nypl_menus_api(method, params)

    def get_dishes_search(self, query, per_page=None, page=None):
        """ GET /dishes/search """
        params = self._paramify_pages(per_page, page)
        params = self._paramify(params, "query", query)

        method = "dishes/search"
        return self.nypl_menus_api(method, params)


if __name__ == "__main__":
    import argparse
    from pprint import pprint

    parser = argparse.ArgumentParser(
        description="Python interface for NYPL's What's on The Menu API.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'token',
        help="Your API token, ask NYPL for one: "
             "https://github.com/NYPL/menus-api#tokens")
    args = parser.parse_args()

    # Example use

    # Initialise the API with your token
    api = WhatsOnTheMenu(args.token)

    # # Get all menus
    # menus = api.get_menus(min_year=1950, max_year=1951)
    # # Pick the first menu
    # print(menus)
    # menu = menus['menus'][0]
    # pprint(menu)

    # # Get a certain menu
    # menu = api.get_menus_id(30924)
    # pprint(menu)

    # # Get pages from a certain menu
    # pages = api.get_menus_id_pages(30924)
    # pprint(pages)

    # # Get pages from a certain menu
    # dishes = api.get_menus_id_dishes(30924)
    # pprint(dishes)

    # Search for meatballs
    dishes = api.get_dishes_search("meatballs")
    pprint(dishes)

    # Show rate limit
    print("Rate limit remaining: ", api.rate_limit_remaining())


# End of file

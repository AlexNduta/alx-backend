#!/usr/bin/env python3
from base_caching import BaseCaching
""" -class that inherits from BaseCaching
    -implements the get and put()
"""


class BasicCache(BaseCaching):
    """ inherits from BaseCaching"""
    def __init__(self):
        self.cache_data = {}
        super().__init__()

    def put(self, key, item):
        """Adds items to the dctionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get items in the dictionary by key"""
        return self.cache_data.get(key)

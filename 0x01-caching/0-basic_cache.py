#!/usr/bin/env python3
""" -class that inherits from BaseCaching
    -implements the get and put()
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching"""

    def put(self, key, item):
        """Adds items to the dctionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ get items in the dictionary by key"""
        return self.cache_data.get(key)

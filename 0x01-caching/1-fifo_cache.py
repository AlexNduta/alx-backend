#!/usr/bin/env python3
""" module level doc"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ class level doc"""
    def __init__(self):
        self.cache_data = {}
        super().__init__()

    def put(self, key, item):
        """ Adds and remove excss items"""
        length = len(self.cache_data)
        if key and item:
            self.cache_data[key] = item
        if length == BaseCaching.MAX_ITEMS:
            first_item = next(iter(self.cache_data.keys()))
            self.cache_data.pop(first_item)
            print("DISCARD:", first_item)

    def get(self, key):
        """Gets items from a  dict"""
        if key:
            return self.cache_data.get(key)
        else:
            return None

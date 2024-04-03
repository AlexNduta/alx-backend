#!/usr/bin/env python3
"""module level documentation"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key and item:

            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS:
               # last_item = next(reversed(self.cache_data.keys()))
                last_item = list(self.cache_data.keys())[-1]
                self.cache_data.pop(last_item)
                print("DISCARD: {}".format(last_item))

            self.cache_data[key] = item


    def get(self, key):
        """gets a list from a dict"""
        if key:
            return self.cache_data.get(key)
        else:
            return None

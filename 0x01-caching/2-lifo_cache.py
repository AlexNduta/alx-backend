#!/usr/bin/env python3
"""module level documentation"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        self.cache_data = {}
        super().__init__()

    def put(self, key, item):
        length = len(self.cache_data)
        if key and item:
            self.cache_data[key] = item

        if length == BaseCaching.MAX_ITEMS:
            last_item = next(reversed(self.cache_data.keys()))

            self.cache_data.pop(last_item)
            print("DISCARD:", last_item)

    def get(self, key):
        """gets a list from a dict"""
        if key:
            return self.cache_data.get(key)
        else:
            return None

import os
import json

APPDIR = os.path.dirname(__file__)


class SimpleCache(object):
    CACHE_FILE = None
    CACHE = {}

    @classmethod
    def exists(cls):
        print("testing for",cls.CACHE_FILE )
        return os.path.exists(cls.CACHE_FILE)

    @classmethod
    def get(cls):
        if not cls.CACHE and cls.exists():
            cls.CACHE = json.load(open(cls.CACHE_FILE))
        return cls.CACHE

    @classmethod
    def set(cls, new_cache):
        cls.CACHE = new_cache
        with open(cls.CACHE_FILE, 'w') as f:
            json.dump(cls.CACHE, f)


class SubscriptionCache(SimpleCache):
    CACHE_FILE = os.path.join(APPDIR, 'cache', 'subscriptions.json')

class PhedexCache(SimpleCache):
    CACHE_FILE = os.path.join(APPDIR, 'cache', 'phedex.json')

import requests
import json
from api_keys import api_keys

class Keyed_Request(requests.Request):
    """Custom class of requests.Request, which requires a 'group' keyword argument and appends the appropriate API key to the headers."""
    def __init__(self,group,**kwargs):
        super().__init__(**kwargs)
        self.headers['OSDI-API-Token'] = api_keys[group]
        
#put, get, post

#people, tags, taggings, 

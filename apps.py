#!/usr/bin/env python
import falcon
import json
from wsgiref import simple_server
 
class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': 'I\'ve always been more interested in the future than in the past.',
            'author': 'Grace Hopper'
        }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(quote)
 
api = falcon.API()
api.add_route('/', QuoteResource())

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8040, api)
    httpd.serve_forever()

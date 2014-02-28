"""
@author: Dimitrios Kanellopoulos
@contact: jimmykane9@gmail.com
"""

from google.appengine.ext import ndb


class Story(ndb.Model):
    title = ndb.StringProperty(required=True)
    vote_count = ndb.IntegerProperty(default = 0)
'''
@author: Dimitrios Kanellopoulos
@contact: jimmykane9@gmail.com
'''
import os
import re
import logging
import config
import json

import webapp2
import jinja2

from google.appengine.ext import ndb
from models.story import Story


class RootPage(webapp2.RequestHandler):
    def get(self):
        story = Story.get_or_insert('Some id or so', title='A voting story again...')
        jinja_environment = self.jinja_environment
        template = jinja_environment.get_template("/index.html")
        self.response.out.write(template.render({'story': story}))


    @property
    def jinja_environment(self):
        jinja_environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                os.path.join(os.path.dirname(__file__),
                             '../views'
                ))
        )
        return jinja_environment


class VoteHandler(webapp2.RequestHandler):
    def post(self):
        logging.info(self.request.body)
        data = json.loads(self.request.body)
        story = ndb.Key(Story, data['storyKey']).get()
        story.vote_count += 1
        story.put()
        self.response.out.write(json.dumps(({'story': story.to_dict()})))


    @property
    def jinja_environment(self):
        jinja_environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                os.path.join(os.path.dirname(__file__),
                             '../views'
                ))
        )
        return jinja_environment


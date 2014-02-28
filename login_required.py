'''
@author: Dimitrios Kanellopoulos
@contact: jimmykane9@gmail.com
'''
from google.appengine.api import users
import webapp2

class LoginRequiredHandler(webapp2.RequestHandler):
    def get(self):
        continue_url = self.request.get('continue')
        self.redirect(users.create_login_url(continue_url))

app = webapp2.WSGIApplication([
        ("/_ah/login_required",LoginRequiredHandler)
    ],debug=True)

import os

import jinja2
import webapp2
from models import Weatherpic
from google.appengine.ext import ndb

# Jinja environment instance necessary to use Jinja templates.
def __init_jinja_env():
    jenv = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=["jinja2.ext.do", "jinja2.ext.loopcontrols", "jinja2.ext.with_"],
        autoescape=True)
    # Example of a Jinja filter (useful for formatting data sometimes)
    #   jenv.filters["time_and_date_format"] = date_utils.time_and_date_format
    return jenv

jinja_env = __init_jinja_env()

PARENT_KEY = ndb.Key("Entity", 'moviequote_root')


class WeatherpicPage(webapp2.RequestHandler):
    def get(self):        
        wpq = Weatherpic.query(ancestor=PARENT_KEY).order(-Weatherpic.last_touch_date_time)
        template = jinja_env.get_template("templates/weatherpic.html")
        self.response.out.write(template.render({"weatherpics_query":wpq}))

class AddPicAction(webapp2.RequestHandler):
    def post(self):        
        new_pic = Weatherpic(parent=PARENT_KEY, image_url=self.request.get('image_url'),caption=self.request.get('caption'))
        new_pic.put()
        self.redirect(self.request.referer)

app = webapp2.WSGIApplication([
    ('/', WeatherpicPage),
    ('/addpic', AddPicAction)
], debug=True)

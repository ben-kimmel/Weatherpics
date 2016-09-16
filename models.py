from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop
from protorpc.messages import Enum


# TODO: Implement




# Potentially helpful (or not) NDB Snippets - For reference only (delete or comment out)
class AccountInfo(ndb.Model):
    """ Information about this user.  There is only 1 of these per user. """

    # Example property for this example model object.
    name = ndb.StringProperty(default="")


class Weatherpic(ndb.Model):
    """ Saves a quote from a movie """
    
    image_url = ndb.StringProperty(default="")
    caption = ndb.StringProperty(default="")
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
    
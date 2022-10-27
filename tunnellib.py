import urllib
import requests
import os
import sys
import time
import exceptions

class tunnellib(object):
    def __init__(self, web):
        self.web = web

    def redirect_traffic(self):
        while True:
            if self.web.startswith('http://'):
                url = self.web.replace('http://', 'https://', 1)
                r = urllib.request.urlopen(self.web)
                return r
            else:
                raise exceptions.WebConfError("Traffic is already redirected to existing SSL server. Try an 'http://'")


    def undo(self):
        if self.web.startswith('http://'):
            url = self.web.replace('http://', 'https://', 1)
            r = urllib.request.urlopen(self.web)
            return r

        else:
            raise exceptions.UndoError("Was not able to undo.")


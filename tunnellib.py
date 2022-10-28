import urllib
import requests
import os
import sys
import time
import exceptions
import webbrowser

class tunnellib(object):
    def __init__(self, web):
        self.web = web

    def secure_connection(self):
        while True:
            if self.web.startswith('http://'):
                url = self.web.replace('http://', 'https://', 1)
                r = urllib.request.urlopen(self.web)
                webbrowser.open(self.web)
            else:
                raise exceptions.WebConfError("Connection is already secured.")


    def unsecure_connection(self):
        if self.web.startswith('http://'):
            url = self.web.replace('http://', 'https://', 1)
            r = urllib.request.urlopen(self.web)
            webbrowser.open(self.web)
        else:
            raise exceptions.WebConfError("Connection is already secured.")
            
    def is_dangerous(self): 
        if self.web.startswith('http://'):
            dangerous = urllib.request.urlopen(self.web)
            if self.web.startswith('http://'):
                print("<CONFIRMED>")
            else:
                print("<UNCONFIRMED>")


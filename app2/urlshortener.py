import httplib2
import logging
import os
import pprint
import sys

from apiclient.discovery import build
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run



# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>
CLIENT_SECRETS = 'client_secrets.json'

# Helpful message to display in the browser if the CLIENT_SECRETS file
# is missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the APIs Console <https://code.google.com/apis/console>.

""" % os.path.join(os.path.dirname(__file__), CLIENT_SECRETS)

# Set up a Flow object to be used if we need to authenticate.
FLOW = flow_from_clientsecrets(CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/urlshortener',
    message=MISSING_CLIENT_SECRETS_MESSAGE)

def shorten(longurl):
  storage = Storage('plus.dat')
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run(FLOW, storage)

  # Create an httplib2.Http object to handle our HTTP requests and authorize it
  # with our good Credentials.
  http = httplib2.Http()
  http = credentials.authorize(http)

  service = build('urlshortener', 'v1', http=http)

  try:

    url = service.url()

    # Create a shortened URL by inserting the URL into the url collection.
    body = {'longUrl':longurl}
    resp = url.insert(body=body).execute()
    return resp['id']

    #short_url = resp['id']

    # Convert the shortened URL back into a long URL
    #resp = url.get(shortUrl=short_url).execute()
    #pprint.pprint(resp)

  except AccessTokenRefreshError:
    return longurl

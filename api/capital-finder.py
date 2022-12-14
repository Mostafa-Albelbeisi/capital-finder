from email import message
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    s = self.path
    url_components = parse.urlsplit(s)
    print(url_components)
    query = parse.parse_qsl(url_components.query)
    dictionary = dict(query)

    '''Here, create a country'''
    if 'country' in dictionary:
        country = dictionary['country']
        url = "https://restcountries.com/v3.1/name/"
        r = requests.get(url + country)
        data = r.json()
        message = f"The capital of {dictionary['country']} is {data[0]['capital'][0]}"

        '''Here, create a capital'''    
    elif 'capital' in dictionary:
        capital = dictionary['capital']
        url = "https://restcountries.com/v3.1/capital/"
        r = requests.get(url + capital)
        data = r.json()
        message = f"{dictionary['capital']} is the capital of {data[0]['name']['common']}"
    else:
        message = "Plese, enter the country or capital"


    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)

        my_dictionary= dict(query_string_list) # from list to dictionary
        # name = my_dictionary.get('name',False) # to git data from my_dictionary and in our cass its "name"
        definisions=[]
        if 'word' in my_dictionary:
            word=my_dictionary['word']
            url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
            r = requests.get(url + word)
            data=r.json()  
            for word_data_definitions in data[0]['meanings'][0]['definitions']:
                definision=word_data_definitions['definition']
                definisions.append(definision)
            message=str(definisions)
        else:
            message='please provide me with a word'


        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()


        self.wfile.write(message.encode())
        return
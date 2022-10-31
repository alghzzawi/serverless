from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s =  self.path # /api/aloha
        url_componaents=parse.urlsplit(s)
        query_string_list=parse.parse_qsl(url_componaents.query)# /api/aloha?query
        my_dictionary= dict(query_string_list) # from list to dictionary


        name = my_dictionary.get('name',False) # to git data from my_dictionary and in our cass its "name"
        if name:
            message=f'Hello {name}'
        else:
            message=f'Hello Stranger'
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())
        return
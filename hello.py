from cgi import parse_qs

def app(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        text = parse_qs(environ['QUERY_STRING'])
        text = text[1 : len(text)]
        text = (text.replace('&', '\n'))
        return [text]
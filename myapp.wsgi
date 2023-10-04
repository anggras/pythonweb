import requests

def application(environ, start_response):
    status = '200 OK'
    # output = b'Hello World!'

    metadata = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
    output = metadata.text

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
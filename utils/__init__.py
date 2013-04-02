import urllib2
import hashlib
from cgi import parse_qs, escape, FieldStorage

def extract_post_data(env):
    post_env = env.copy()
    post_env['QUERY_STRING'] = '' # as to not have any  querystring data permeate into our post_data
    post_data = FieldStorage(
        fp=post_env['wsgi.input'],
        environ=post_env,
        keep_blank_values=True
    )
    return post_data

def compute_sha1_of_text(text):
    cat1 = hashlib.sha1()       # init sha1 object
    cat1.update(text)           
    return cat1.hexdigest()

def get_url_body(url):
    response = urllib2.urlopen(url)
    body = response.read()
    return body
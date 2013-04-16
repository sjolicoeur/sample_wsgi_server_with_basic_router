import simplejson
import memcache
from utils.decorators import render_response_as_json
from utils import  extract_post_data
from utils.fibonacci import fib
from utils import  compute_sha1_of_text, get_url_body
import random

def paige404(env, start_response): # named after the roller derby athlete
    msg1 = """
        <p>Maybe you should think about doing some time travel ... 
        <blink>"001100010010011110100001101101110011"</blink></p>"""
    msg2 = """<p>The meaning of life is 42</p>"""
    show_msg = random.choice([msg1, msg2])
    start_response('404 Not Found', [('Content-Type', 'text/html')])
    return ["""
    <h1>Not Found</h1>
    <br>
    {}
    """.format(show_msg)]


@render_response_as_json
def get_fib(env, start_response, num):
    num = int(num)
    fib_result =  fib(num)
    return {"response": fib_result}


@render_response_as_json
def google_body_fetcher(env, start_response):
    data = get_url_body("http://google.com")
    sha1_encoded_data = compute_sha1_of_text(data)
    return { "response" : sha1_encoded_data }


@render_response_as_json
def store_service(env, start_response):
    data = None
    key = "value"
    data_store = memcache.Client(['127.0.0.1:11211'], debug=0)
    request_method = env['REQUEST_METHOD']
    if request_method.lower() == "post":
        post_data = extract_post_data(env)
        data = post_data[key].value
        result = data_store.set(key, data)
        return {"stored" : result, "response" : data }
    return {"response" : data_store.get(key) }

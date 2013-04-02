from functools import wraps
import memcache
import simplejson


def cache(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # compose key
        # get from cache
        # if not in cache compute and set in cache
        key_items = ["__",f.__name__] 
        [key_items.extend(str(item)) for item in args]
        [key_items.extend(group) for group in kwargs.items()]
        
        cache_key = "_".join(key_items)
        print 'Cache key : ', cache_key
        data_store  = memcache.Client(['127.0.0.1:11211'], debug=0)
        result = data_store.get(cache_key)
        if not result :
            print "not in cache compute it"
            result = f(*args, **kwargs)
            print "result is : " , result
            data_store.set(cache_key, result)
        return result
    return wrapper

def render_response_as_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        start_response = args[1] # tis a position arg so start_response is number 2 
        payload = f(*args, **kwargs)
        start_response('200 OK', [('Content-Type', 'application/json')])
        json_encoded_payload = simplejson.dumps(payload)
        return [ json_encoded_payload ]
    return wrapper
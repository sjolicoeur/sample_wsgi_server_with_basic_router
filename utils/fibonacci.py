from utils.decorators import cache

@cache
def fib(num):
    # make sure we get an int
    assert type(num) == int, "num should be an int it was : {}".format( type(num) )
    if num in  [0, 1] :
        return num
    else :
        return fib(num-1)+fib(num-2)
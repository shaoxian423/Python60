def cache(func):
    _cache = {}

    def wrapper(x):
        if x not in _cache:
            _cache[x] = func(x)
        return _cache[x]
    return wrapper


@cache
def slow_square(x):
    print(f"Computing {x}^2")
    return x*x

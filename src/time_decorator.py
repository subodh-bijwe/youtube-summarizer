import time
def timeit(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = function(*args, **kwargs)
        end = time.time()
        print(f"Function '{function.__name__}' executed in {end - start:.4f} seconds")
        return res
    return wrapper
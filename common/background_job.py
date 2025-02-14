"""
Run funktions in the background decorator for Django.
"""

import threading
from functools import wraps


def run_in_background(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
    return wrapper


"""
Example usege:

@run_in_background
def my_function():
    print("Hello world!")

"""
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def add(a, b):
    print(a + b)

add(1, 2)


def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def add(a, b):
    print(a + b)

add(1, 2)


import logging

def log_execution(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_execution
def process_data(data_id):
    # Imagine database logic here
    return f"Data {data_id} processed"



import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f} seconds")
        return result
    return wrapper

@time_it
def heavy_computation():
    time.sleep(2) # Simulate work
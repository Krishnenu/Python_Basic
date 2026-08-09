# def decoratorfn(fn):
#     def wraper(*args,**kwargs):
#         result=fn(*args,**kwargs)
#         return result
#     return wraper


# @decoratorfn
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# greet("Alice", greeting="Welcome")
# from functools import wraps
# from time import time


# def retry(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         for attempt in range(1, 4):
#             try:
#                 return fn(*args, **kwargs)
#             except Exception as e:
#                 print(f"⚠️ Attempt {attempt} failed: {e}")
#                 if attempt == 3:
#                     raise Exception("Retry limit reached")
#     return wrapper


# @retry
# def retryLogic(promt):
#     print(promt)
#     raise ConnectionError("Server unavailable")

# retryLogic("hellow")
# retryLogic("hellow")
# retryLogic("hellow")

# retryLogic("hellow")
# retryLogic("hellow")
# retryLogic("hellow")



# def decocarator(fn):
#     def wrapper(*args,**kwargs):
#         print("before")
#         result=fn(*args,**kwargs)
#         print("after")
#         return result
#     return wrapper


# @decocarator
# def greet(name):
#     return name

# h1=greet("hwllo")

# print(h1)

def decocarator(fn):
    def wrapper(*args,**kwargs):
        print("before")
        result=fn(*args,**kwargs)
        print("after")
        return result
    return wrapper


@decocarator
def greet(name):
    return name

h1=greet("hwllo")

print(h1)





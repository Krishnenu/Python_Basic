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



# Empty dictionary
empty_dict = {}
empty_dict_alt = dict()

# Dictionary with initial values
student = {"name": "Alice", "age": 22, "major": "Computer Science"}

print(student.get('name'))


squares = [x**x for x in range(1, 4)]


# print(squares)

# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 99, "c": 4}

# print(dict1 | dict2)

# scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# print(sorted(scores.items()))
# print(sorted(scores.items(), key=lambda x: x[1]))
# print(sorted(scores, key=lambda name: scores[name]))


inp="Hi I am Krishnendu Narayan"

# opt={hi:2,i:1,:am:2,Krishnendu:10,narayan:7}
# xt=[{'Hi': 2}, {'I': 1}, {'am': 2}, {'Krishnendu': 10}, {'Narayan': 7}]
xt = [{'Hi': 2}, {'I': 1}, {'am': 2}, {'Krishnendu': 10}, {'Narayan': 7}]

print(next(iter(xt[0].values())))

def count_l(str):
    new_str = str.split(' ')
    d = []
    for w in new_str:
        n = {}
        n[w] = len(w)
        d.append(n)
    return sorted(d, key=lambda x: next(iter(x.values())))
    # def get_value(item):
    #     return list(item.values())[0]

    # return sorted(d, key=get_value)

print(count_l(inp))
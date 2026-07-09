# decorators

def decorator_function(original_function):
    def wrapper_function():
        print("hellow code executed before wrapper")
        return original_function()
    return wrapper_function

def display():
    print("display function run")


decorated_display=decorator_function(display)
decorated_display()
#-------------------------------------------------------------------------------

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('hellow code executed before wrapper {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function


@decorator_function
def display():
    print("display function run")

@decorator_function
def display_info(name,age):
    print('display name: {} and age : {}'.format(name,age))

display()

display_info("krish",30)


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.info)

    def wrapper(*args,**kwargs):
        logging.info('Ran with args: {},and kwargs: {}'.format(args,kwargs))
        return orig_func(*args,**kwargs)

    return wrapper




# decorator class----------------------------------
# class decorator_class(object):
#     def __init__(self,original_function):
#         self.original_function=original_function

#     def __call__(self, *args, **kwargs):
#         print('call method executed before wrapper {}'.format(self.original_function.__name__))
#         return self.original_function(*args,**kwargs)


# @decorator_class
# def display_info(name,age):
#     print('display name: {} and age : {}'.format(name,age))

# display_info("Anu",43)


# ------------------------------------------------------------
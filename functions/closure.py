# A closure is an inner function that retains access to the variables 
# of its enclosing (outer) function even after the outer function 
# has completed execution.


def outer_function():
    message="hi"

    def inner_function():
        print(message)

    return inner_function

my_func=outer_function()

print(my_func.__name__,my_func)
my_func()

#--------------------------------------------------
def outer():

    x = 100

    def inner():
        print(x)

    return inner

f = outer() # inner function refrence / return inner function

f()



#------------------------------------------

def outer_function(msg):
    message=msg

    def inner_function():
        print(message)

    return inner_function # acts as first class functions

hi_func=outer_function("Hi")
hellow_funtion=outer_function("hellow")

hi_func()
hellow_funtion()

# HOC

def square(num):
    return num*num

def my_map(func,arg_list):
    result=[]
    for i in arg_list:
        result.append(func(i))
    return result

squares=my_map(square,[1,2,3,4,5,6])

print(squares)
# local(variable in scope of fucntion) 
# enclosing(variable within local scope of fucntion) 
# global (varibale defined at top level)
# Builtin 
# (LEGB)


# global and local

# x='global x'

def text():
    # y="local_y"
    # x=9
    # print(y)
    global x # explicity changing the scope of local variable dont use it 
    x="local_x"
    print(x)


text()
# print(y) not accessible
print(x)


def test1(z):
    print(z)


test1("local scope z")

#-----------------------------------------------------------------------------------------
#build in 
import builtins

m=min([5,1,2,4])
print(m)

# print(dir(builtins))



#---------------------------------------------------------------

def outer():
    x="outer x"
    def inner():
        nonlocal x # acts as inner x affecting local x of outer function
        # x='inner x' //inclosing scope is outer function
        print(x)

    inner()
    print(x)

outer()




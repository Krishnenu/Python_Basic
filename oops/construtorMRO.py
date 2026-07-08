
class X:
    def __init__(self):
        print("init A")

    def feature1(self):
         print("working feature 1")

    def feature2(self):
        print("working feature 2")

class Y(X):
# by deafult if b constructor is there then it will call b else it will call parent constructor if present
    def __init__(self): 
        super().__init__()
        print("init b")
    
    def feature3(self):
        print("working feature 3")



# in case of multiple inheretence
class I:
    def __init__(self):
        print("I init")

    def feature(self):
        print("working feature I")

class J:
    def __init__(self):
        print("J init")
        
    def feature(self):
        print("working feature J")

# MRO method resolution order left to right
class K(I,J):
    def __init__(self):
        super().__init__()
        print("K init")

    def feature6(self):
        print("working feature 6")

a=X()
b=Y()

# create object of multiple inheretence

c=K()
c.feature()

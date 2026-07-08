# duck typing
# method overloading
# method overriding
# operator overriding

# duck typing /dynamic typing

# x =5 change it so "navin"

#duck typing
class PyCharm:
    def execute(self):
        print("compiling")
        print("runnig")

class Editor:
    def execute(self):
        print("Spellcheck")
        print("typocheck")
        print("compiling")
        print("runnig")

class Laptop:
    def code(self,ide):
        ide.execute()


ide =PyCharm()
editor=Editor()

lap1=Laptop()

lap1.code(editor)

# operator overloading -----------------------------------------------------------------------------------

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3

    def __gt__(self,other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2

        return s1>s2

    def __str__(self):
        print(self.m1,self.m2)


s1=Student(58,79)
s2=Student(60,23)

s3=s1+s2

print(s3.m1)

print(s1.__gt__(s2))


# operator overriding
a=9
print(a.__str__())

s1.__str__()



#Method overloading ------------------------------------------------------------------------------------------------


class College:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self, a=None, b=None, c=None):

        if a is not None and b is not None and c is not None:
            return a + b + c

        elif a is not None and b is not None:
            return a + b

        elif a is not None:
            return a

        return 0


c= College(56,99)
print(c.sum(67,8))
print(c.sum(67,89,8))



# method overriding 


class A:
    def show(self):
        print("in show A")

class B(A):
    def show(self):
        print ("in show B")


a1=B()

a1.show()
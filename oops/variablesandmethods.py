# instance variable and class / static variable

class car:
    # class variable 
    wheels=4

    def __init__(self):
        # intance variable
        self.mil=10
        self.com="BMW"

c1=car()
c2=car()

c1.mil=90
print(c1.com,c1.mil,c1.wheels) 
print(c2.com,c2.mil,c2.wheels) 

car.wheels=5
print(c1.com,c1.mil,c1.wheels) 
print(c2.com,c2.mil,c2.wheels) 



#----------------------------------------------------------------------------------------------------


#methods instance , class method and static methods

class student:

    # class variable 
    school="DAV"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3


    # instance method 1. acccessor 2. mutator like getter and setter
    def average(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,val):
        self.m1=val


    # class variable class method 
    @classmethod
    def getschool(cls):
       return cls.school

    # static method want to do extra with class
    @staticmethod
    def info():
        print("this is school")



s1 = student(34,32,89)
s2=student(65,89,22)

print(s1.average())
print(s2.average())

#print(student.getschool()) without  decorator it throw error 

print(student.getschool())

student.info()

    
class student:
    # varibale declaration 

    #default constructor case
    # def __init__(self):
    #     self.info="Rakesh"
    #     self.age=39

    # constructor is used to initalise varibales and called automatically when we create object
    def __init__(self,name,house):
        self.name=name
        self.house=house

    def get_name(self):
        return self.name

# default constructor case
# defaltC=student()
# defaltC2=student()

# defaltC.info="Krish"

# print(defaltC.info)
# print(defaltC2.info)

    
a =student("krishne","myhome")

student.get_name(a) # normally we wont use this type of syntex

print (type(a)) # <class '__main__.student'>

print(a.get_name())

class ParentA:
    def method_a(self):
        return "Method from Parent A"

class ParentB:
    def method_b(self):
        return "Method from Parent B"

# can extends two class and we can call methods of both class by creating object
class Child(ParentA, ParentB):
    pass

# Useage
obj = Child()
print(obj.method_a())  # Output: Method from Parent A
print(obj.method_b())  # Output: Method from Parent B


class myName:
    def __init__(self, age):
        self.age=age
    def update(self,age):
        self.age=age
    def get_age(self):
        return self.age

c1=myName(39)
c1.update(90)
# print(c1.update(56))
print(c1.get_age())
c1.age=65
print(c1.get_age())
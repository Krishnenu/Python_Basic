class student:

    def __init__(self,name,house):
        self.name=name
        self.house=house
    def get_name(self):
        return self.name
    
a =student("krishne","myhome")

print(a.get_name())

class ParentA:
    def method_a(self):
        return "Method from Parent A"

class ParentB:
    def method_b(self):
        return "Method from Parent B"

class Child(ParentA, ParentB):
    pass

# Usage
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

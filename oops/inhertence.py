class Parent:
    def feature1(self):
        print("working feature 1")

    def feature2(self):
            print("working feature 2")



class Child(Parent):
    def feature3(self):
        print("working feature 3")
     
    def feature4(self):
        print("working feature 4")

# multi level inheritence
class OtherChild(Child):
     def feature5(self):
        print("working feature 5")

# supports multiple inheretence too

class X:
     def feature6(self):
        print("working feature 6")

class Y:
     def feature7(self):
        print("working feature 7")

class Z(X,Y):
     def feature8(self):
        print("working feature 8")

a=Parent()

a.feature1()
a.feature2()

b=Child()

b.feature3()
b.feature4()

# what if we want feature of parent in child
# single level inheretence

b.feature2()
b.feature1()

# multilevel inheritence
d=Z()

d.feature6()
d.feature7()
d.feature8()
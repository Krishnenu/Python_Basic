# class inside a class

class Student:
    def __init__(self, name , roolNo):
        self.name=name
        self.roolNo=roolNo
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.roolNo)



    class Laptop:
        def __init__(self):
            self.brand="Hp"

s1= Student("Naryan",236)
s2 = Student("David",78)

s1.show()
print(s1.lap.brand)


lap1=Student.Laptop()


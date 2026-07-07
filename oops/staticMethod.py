class Student:
    school="abc" # Static method
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,m1):
        self.m1=m1

    @classmethod
    def school_name(cls):
        return Student.school

    @staticmethod
    def info():
        print("this is my school")

s1=Student(34,54,31)
s2=Student(98,76,32)

print(s1.average())
print(s2.average())


print(Student.school_name())

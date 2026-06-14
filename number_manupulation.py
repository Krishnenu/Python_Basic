import math
import random

x=2
y=3
z=4

print((x+y)*z)

print(float(40)+23.3)
print(float(54))

print((x,y,z))

print(4**4)

result=1/3

print(result)

print(1<4)

print(4!=5.0)

print(x<y<z)
# and & or ||
print(x<y and y<z)

print (1==2<3) # 1==2 & 2<3

# ops with math lib

print(math.floor(3.9),math.floor(-3.5))

print(math.trunc(2.8),math.trunc(-2.8))

print((2+1j)*3)

print(0o20,oct(64))
print(0xff,hex(64))
print(0b1000,bin(1000))


int('64',8)  # convert to octal

#bit wise operation
x=1

print(x<<4)

# random library
print(random.random(),random.randint(1,10))

l1=['hi','hellow','me','apple']

print(random.choice(l1))
print(random.choice(l1))
random.shuffle(l1)
print(l1)
random.shuffle(l1)
print(l1)

# decimal contex manager

print(0.1+0.1+0.4,(0.1+0.1+0.4)-0.3)

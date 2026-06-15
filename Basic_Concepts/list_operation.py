# list in python is array in other lang


fruits=["apple","orange","grape","banana","lichi"]

print(fruits,fruits[1],fruits[:3],len(fruits))

fruits[3]="beery"

print(fruits)

fruits[1:2]=["papaya"]
print(fruits)

fruits[1:3]=["gauva","mango"]

print(fruits)

# inserting
fruits[1:1]=["test","test"]

print(fruits)

fruits[1:3]=[] #inserting nothing means deleting

print(fruits)

for fruit in fruits:
    print(fruit,end=",")

if "payaya" in fruits:
    print("i have")

if "lichi" in fruits:
    print("i have")

fruits.append("papaya")

if "papaya" in fruits:
    print("i have")

print(fruits.pop())

print(fruits)

fruits.remove("mango")

print(fruits)

fruits.insert(2,"orange")

print(fruits)

fruits_copy=fruits.copy()

print(fruits_copy.append("lemon")) # different referency is allocated to copy 

print(fruits,fruits_copy)

# list comprehansion (we can write loop in array also)
print(range(10))

squared_nums=[x**2 for x in range(10)]

print(squared_nums)

cube_num=[y**3 for y in range(10)]

print(cube_num)
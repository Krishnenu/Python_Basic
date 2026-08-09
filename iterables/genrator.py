# def count_up_to(max_value):
#     current = 1
#     while current <= max_value:
#         yield current
#         current += 1

# # Usage
# counter = count_up_to(3)
# print(next(counter))  # 1
# print(next(counter))  # 2

def count_up_to(value):
    current=1
    while current <= value:
        yield current
        current+=1

c1=count_up_to(5)
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))


def accumulato():
    while True:
        val=yield total
        if val is not None:
            val+=value

gen=accumulato(0)
print(next(gen))

print(gen.send(20))
print(next(gen))

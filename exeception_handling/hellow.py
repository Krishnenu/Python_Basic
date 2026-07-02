# while True:
#     try:
#         x= int(input("what is x? "))
#     except ValueError:
#         print("X is not number")
#     else:
#         break
# print(f"x is {x}")

# while True:
#     try:
#         x= int(input("what is x? "))
#         break
#     except ValueError:
#         print("X is not number")

# print(f"x is {x}")

# def main():
#     x=get_int()
#     print(x)

# def get_int():
#     while True:
#         try:
#             x= int(input("what is x? "))
#         except ValueError:
#             print("X is not number")
#         else:
#             break
#     return x

# main()


# while True:
#     try:
#         x= int(input("what is x? "))
#     except ValueError:
#        pass
#     else:
#         print(f"x is {x}")
#         break

def main():
    x=get_int("what is x? ")
    print(x)

def get_int(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            pass

main()
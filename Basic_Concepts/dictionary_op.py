info_type={"first":"krishnendu","second":"narayan","city":"blr","pin":"560066"}

print(info_type)

print(info_type.get("first"))

info_type["pin"]="560087"

print(info_type)

for info in info_type:
    print(info,info_type[info])

for  key,value in info_type.items():
    print(key,value)

if "first" in info_type:
    print("yes i have")

print(len(info_type))

info_type["area"]="urban"
print(info_type)

info_type.pop("pin")

print(info_type)

info_type.popitem()

print(info_type)

del info_type["city"]

print(info_type)

info_copy=info_type.copy()

print(info_type,info_copy)

info_copy["city"]="blr"

print(info_type,info_copy)

tea_shop ={
    "chai":{"masala":"spicy","ginger":"zusty"},
    "tea":{"green":"freash","black":"strong"}
}

print(tea_shop["chai"]["ginger"])

squared_num={x:x**2 for x in range(6)}

print(squared_num)

squared_num.clear()
print(squared_num)


keys=["apple","lemon","banana"]
default_val="delicious"

new_dict=dict.fromkeys(keys,default_val)

print(new_dict)

new_dict=dict.fromkeys(keys,keys)

print(new_dict)
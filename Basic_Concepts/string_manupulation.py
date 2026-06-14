# string ' ' ,"" ,""""""

str="Krishnendu Narayan"
first_char=str[0]

print(str,first_char)

slicedName=str[0:11]

print(slicedName)

num_list="0123456789"

# num_list[0:7:2] print in hoopping of 2
# strip act as trim a/c to other lang

print(num_list[:],num_list[3:],num_list[:7],num_list[0:7:2],num_list[0:7:3])

print(str.strip(), str.capitalize(),str.upper(),str.lower())

print(str.replace("Narayan", "Krishnendu"))
print(str)

str2="Krishnendu, Amit, Anurag, Nirala, Kuldeep"

print(str2.split(",")) #convert it to set also
print(str2)

print(str.find("Krishnendu"))

strnew='i ordered a {} products on amazon'

print(strnew.format(3))

str4=["apple","Orage","banana","grapes"]
print(", ".join(str4))

print(len(str))

for letter in str:
    print(letter)

str5="He said, \"you are good\" " 

print(str5)


str6='krishnendu\nnarayan'
# to avoid \n
print(str6)

str7=r"krishnendu\nnarayan"

print(str7)

print("Krishnendu" in str)
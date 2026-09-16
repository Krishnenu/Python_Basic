# Empty dictionary
empty_dict = {}
empty_dict_alt = dict()

# Dictionary with initial values
student = {"name": "Alice", "age": 22, "major": "Computer Science"}

print(student.get('name'))


squares = [x**x for x in range(1, 4)]


# print(squares)

# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 99, "c": 4}

# print(dict1 | dict2)

# scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# print(sorted(scores.items()))
# print(sorted(scores.items(), key=lambda x: x[1]))
# print(sorted(scores, key=lambda name: scores[name]))


inp="Hi I am Krishnendu Narayan"

# opt={hi:2,i:1,:am:2,Krishnendu:10,narayan:7}
# xt=[{'Hi': 2}, {'I': 1}, {'am': 2}, {'Krishnendu': 10}, {'Narayan': 7}]
xt = [{'Hi': 2}, {'I': 1}, {'am': 2}, {'Krishnendu': 10}, {'Narayan': 7}]

print(next(iter(xt[0].values())))

def count_l(str):
    new_str = str.split(' ')
    d = []
    for w in new_str:
        n = {}
        n[w] = len(w)
        d.append(n)
    return sorted(d, key=lambda x: next(iter(x.values())))
    # def get_value(item):
    #     return list(item.values())[0]

    # return sorted(d, key=get_value)

print(count_l(inp))
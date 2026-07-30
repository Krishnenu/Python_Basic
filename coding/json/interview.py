arr=[{
    "name":"abc","price":289
},{
    "name":"ebc","price":403
},{
    "name":"gbc","price":3092
}]


def findmax(arr):
    max=0
    for j in arr:
        if j['price']>max:
            max=j['price']
    return max


print(findmax(arr))
#Q1

logs = [
    "Auth: ERROR",
    "Payment: INFO",
    "Auth: INFO",
    "Payment: ERROR",
    "Auth: ERROR"
]

{
    "Auth": {"ERROR": 2, "INFO": 1},
    "Payment": {"INFO": 1, "ERROR": 1}
}


def distinonary(logs):
    dist={}
    for log in logs:
        name,msg=log.split(":",1)
        msg = msg.strip()
        if not name in dist:
            dist[name]={}
        if name in dist:
            dist[name][msg]=dist[name].get(msg,0)+1
    return dist

print(distinonary(logs))


#Q 2

data = {
    "user": {
        "name": "Alice",
        "address": {
            "city": "Bangalore",
            "pin": 560001
        }
    }
}


{
"user.name":"Alice",
"user.address.city":"Bangalore",
"user.address.pin":560001
}

def flatObj(data):
    for d in data:
        
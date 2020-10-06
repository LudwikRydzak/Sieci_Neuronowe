import random
def generate(_amount):
    result = []
    for i in range(_amount):
        a = random.random()/100
        b = random.random()/100
        result.append([-1,a,b])
        result.append([-1,a+b,a-b])
        result.append([-1,b,a])
        result.append([1,1-a,1-b])
    return result



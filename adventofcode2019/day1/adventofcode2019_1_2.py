import math

path = 'data.txt'
mass_file = open(path,'r')
data = mass_file.read().splitlines()
i = 1
suma = 0
ss=[12]

def sumator(data):
    ss = []
    for i in data:
        s = math.floor(int(i)/3)-2
        if s <= 0:
            s = 0
        ss.append(s)
    return ss


while sum(ss) != 0:
    ss = sumator(data)
    suma += sum(ss)
    print('---')
    print(ss)
    print(suma)
    data = ss


mass_file.close()



path = 'data8.txt'
mass_file = open(path,'r')
data = mass_file.read().splitlines()
data = data[0]
print(data)
print(len(data))
print('-------')
a = 0
l = 0
z = 25
layer = []
layers = []
for i in range(len(data)):
    if l < 6:
        line = list(data[a:z])
        if line != []:
            layer.append(line)
        l += 1
        a += 25
        z += 25
        print(layer)
    else:
        l = 0
        layers.append(layer)
        layer = []





print(layers)

mass_file.close()
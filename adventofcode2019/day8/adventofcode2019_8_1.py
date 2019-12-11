path = 'data8.txt'
mass_file = open(path,'r')
data = mass_file.read().splitlines()
data = data[0]
print(data)
print(len(data))
print('-------')
a, z = 0, 150
layers = []
layers_tmp = []
layers_tmp2 = []
for i in range(100):
    line = data[a:z]
    layers.append(line)
    a += 150
    z += 150
for i in range(100):
    a, z = 0, 25
    for j in range(6):
        line = layers[i][a:z]
        layers_tmp.append(line)
        a += 25
        z += 25
print(layers)
min = 99
multi = 0
for i in range(len(layers)):
    zero = list(layers[i]).count('0')
    one = list(layers[i]).count('1')
    two = list(layers[i]).count('2')
    if zero < min:
        min = zero
        multi = one*two
print(multi)

'''
layers = []
a, z = 0, 6
for i in range(100):
    line = layers_tmp[a:z]
    layers.append(line)
    a += 6
    z += 6
print(layers)
'''







mass_file.close()
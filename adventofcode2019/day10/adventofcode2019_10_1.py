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
#print(layers)
layers = []
a, z = 0, 6
for i in range(100):
    line = layers_tmp[a:z]
    layers.append(line)
    a += 6
    z += 6
print(layers)
picture = []
pixel = ' '
line = ''
for j in range(0,6):
    for i in range(0,25):
        for k in range(0,100):
            if layers[k][j][i] == '2' and pixel != '1' and pixel != '0' and pixel != '2':
                pixel = '2'
            elif layers[k][j][i] == '1' and pixel != '0':
                pixel = '1'
            elif layers[k][j][i] == '0' and pixel != '1':
                pixel = '0'
        if pixel == '1':
            pixel = '*'
        elif pixel == '0':
            pixel = ' '
        elif pixel == '2':
            pixel = '.'
        line += pixel
        pixel = ' '
    picture.append(line)
    line = ''
for i in picture:
    print(i)
mass_file.close()
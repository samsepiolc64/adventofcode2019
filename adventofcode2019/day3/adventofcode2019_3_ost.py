import math

path1 = 'data3.txt'
path2 = 'data3_2.txt'
mass_file1 = open(path1,'r')
mass_file2 = open(path2,'r')
for line in mass_file1.readlines():
    data1 = line.rstrip().split(',')
for line in mass_file2.readlines():
    data2 = line.rstrip().split(',')

def move(data):
    skid = []
    x, y = 0, 0
    for i in data:
        if i[0] == "R": x+=int(i[1:])
        elif i[0] == "L": x-=int(i[1:])
        elif i[0] == "U": y+=int(i[1:])
        elif i[0] == "D": y-=int(i[1:])
        skid.append([x,y])
    return skid

def cross(skid1,skid2):
    sum = []
    print('krosuje')
    common = [i for i in skid1 if i in skid2]
    print(common)
    for i in common:
        print(i)
        sum.append(abs(i[0])+abs(i[1]))
    sum.remove(0)
    return min(sum)

def grow(skid):
    tmpskid = skid.copy()
    for i in range(len(skid)-1):
        print(i)
        k = skid[i+1][0]-skid[i][0]
        if k != 0:
            if k > 0:
                for s in range(skid[i][0]+1, skid[i][0]+abs(k)):
                        tmpskid.append([s, skid[i][1]])
            else:
                for s in range(skid[i+1][0]+1, skid[i+1][0]+abs(k)):
                    tmpskid.append([s, skid[i][1]])
        l = skid[i+1][1]-skid[i][1]
        if l != 0:
            if l > 0:
                for t in range(skid[i][1]+1, skid[i][1]+abs(l)):
                    tmpskid.append([skid[i][0], t])
            else:
                for t in range(skid[i+1][1]+1, skid[i+1][1]+abs(l)):
                    tmpskid.append([skid[i][0], t])
    return tmpskid

print('start')
skid1 = move(data1)
skid2 = move(data2)
skid1 = grow(skid1)
skid2 = grow(skid2)
wynik = cross(skid1,skid2)
print(wynik)

mass_file1.close()
mass_file2.close()
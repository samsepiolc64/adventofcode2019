import math

path1 = 'data3.txt'
path2 = 'data3_2.txt'
mass_file1 = open(path1, 'r')
mass_file2 = open(path2, 'r')
for line in mass_file1.readlines():
    data1 = line.rstrip().split(',')
for line in mass_file2.readlines():
    data2 = line.rstrip().split(',')


def move(data):
    skid = []
    x, y = 0, 0
    for i in data:
        if i[0] == "R":
            x += int(i[1:])
        elif i[0] == "L":
            x -= int(i[1:])
        elif i[0] == "U":
            y += int(i[1:])
        elif i[0] == "D":
            y -= int(i[1:])
        skid.append([x, y])
    return skid


def cross(skid1, skid2):
    sum = []
    print('crosuje')
    minsum = 999000
    common = [i for i in skid1 if i in skid2]
    '''
    for i in common:
        sum.append(abs(i[0])+abs(i[1]))
        if 0 != (abs(i[0])+abs(i[1])) < minsum:
            minsum = abs(i[0])+abs(i[1])
            punkt = [abs(i[0]), abs(i[1])]
    sum.remove(0)
    #return min(sum)

    return(punkt)
    '''
    return (common)


def grow(skid):
    tmpskid = skid.copy()
    j = 0
    for i in range(len(skid) - 1):
        # print(tmpskid)
        k = skid[i + 1][0] - skid[i][0]
        if k != 0:
            if k > 0:
                for s in range(skid[i][0] + 1, skid[i][0] + abs(k)):
                    tmpskid.insert(j + 1, [s, skid[i][1]])
                    j += 1
                    # tmpskid.append([s, skid[i][1]])
            else:
                for s in range(skid[i + 1][0] + abs(k) - 1, skid[i + 1][0], -1):
                    tmpskid.insert(j + 1, [s, skid[i][1]])
                    j += 1
                    # tmpskid.append([s, skid[i][1]])
        l = skid[i + 1][1] - skid[i][1]
        if l != 0:
            if l > 0:
                for t in range(skid[i][1] + 1, skid[i][1] + abs(l)):
                    # tmpskid.append([skid[i][0], t])
                    tmpskid.insert(j + 1, [skid[i][0], t])
                    j += 1
            else:
                for t in range(skid[i + 1][1] + abs(l) - 1, skid[i + 1][1], -1):
                    # tmpskid.append([skid[i][0], t])
                    tmpskid.insert(j + 1, [skid[i][0], t])
                    j += 1
        j += 1
    # print(tmpskid)
    return tmpskid


def steps(wynik, skid1, skid2, licznik):
    # print(wynik)
    # print(skid1)
    # print(skid2)
    e = licznik
    j, k = 0, 0
    for i in skid1:
        if i == wynik[e]:
            break;
        else:
            j += 1
    for i in skid2:
        if i == wynik[e]:
            break;
        else:
            k += 1

    return [j, k]


print('start')
skid1 = move(data1)
skid2 = move(data2)
print(skid1)
print(skid2)
skid1 = grow(skid1)
skid2 = grow(skid2)
wynik = cross(skid1, skid2)
end = []

for i in range(len(wynik)):
    wynik = steps(wynik, skid1, skid2, 1)
    sumka = sum(wynik)
    end.append(sumka)


print(min(end))

mass_file1.close()
mass_file2.close()
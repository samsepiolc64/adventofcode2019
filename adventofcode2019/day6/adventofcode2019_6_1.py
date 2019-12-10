path = 'data6.txt'
orbits = []
tab_orb = []
tab_orbs = []
mass_file = open(path,'r')
for line in mass_file.readlines():
    data = line.rstrip().split(')')
    orbits.append(data)
first_orb = [x for x in orbits if x[0] == 'COM']
first_orb = first_orb[0]

j = 0
koniec = False
while not koniec:
    if j == 0:
        tab_orb.append(first_orb)
        j = 1
    result = any(elem[0] == tab_orb[-1:][0][1] for elem in orbits)
    if result:
        for i in orbits:
            if tab_orb[-1:][0][1] == i[0]:
                tab_orb.append(i)
                result2 = any(elem[0] == i[1] for elem in orbits)
                if not result2:
                    orbits.remove(i)
    else:
        j = 0
        if len(tab_orb)>1:
            tab_orbs.append(tab_orb)
        else:
            koniec = True
        tab_orb = []

sum = 0
for elem in tab_orbs:
    sum += len(elem)
    print(elem)
print(sum)

mass_file.close()
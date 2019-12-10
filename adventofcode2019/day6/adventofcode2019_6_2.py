from collections import Counter

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

t1, t2 = [],[]
for elem in tab_orbs:
    if elem[-1:][0][1] == 'YOU':
        t1 = elem
    if elem[-1:][0][1] == 'SAN':
        t2 = elem
t3 = t1 + t2


for g in t3:
    if t3.count(g) > 1:
        t3 = [x for x in t3 if x != g]
        print(t3)

print(len(t3)-2)

mass_file.close()
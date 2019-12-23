def Data():
    path = 'data10.txt'
    mass_file = open(path,'r')
    data = mass_file.read().splitlines()
    return data


    mass_file.close()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def is_between(self, c):
        def cmp(a, b):
            return (a > b) - (a < b)
        a, b = self.a, self.b
        return ((b.x - a.x) * (c.y - a.y) == (c.x - a.x) * (b.y - a.y) and
                abs(cmp(a.x, c.x) + cmp(b.x, c.x)) <= 1 and
                abs(cmp(a.y, c.y) + cmp(b.y, c.y)) <= 1)
def Data2XY(data):
    xylist = []
    for i in range(0,len(data)):
        for j in range(0,len(data[0])):
            if data[j][i] == '#':
                xylist.append((i,j))
    return(xylist)

def Detect(data):
    maxlicznik = 0
    rozmiar= len(data)-1
    for i in data:
        licznik = 0;
        data2 = data.copy()
        data3 = data.copy()
        for j in data2:
            for k in data3:
                a = Point(i[0], i[1])
                b = Point(j[0], j[1])
                c = Point(k[0], k[1])
                if i != j != k != i:
                    colision = Segment(a, b).is_between(c)
                    #print(i,j,k,Segment(a, b).is_between(c))
                    if colision:
                        licznik += 1
                        data3.remove(k)
        if (rozmiar-licznik) > maxlicznik:
            maxlicznik = rozmiar-licznik
            punkt = i
    return((punkt,maxlicznik))



data = Data()
data = Data2XY(data)

data = Detect(data)
print(data)



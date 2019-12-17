path = 'data10.txt'
mass_file = open(path,'r')
data = mass_file.read().splitlines()


'''
det:=a.x*b.y+b.x*c.y+c.x*a.y-c.x*b.y-a.x*c.y-b.x*a.y;
if det<>0 then showmessage('Punkt C NIE należy do odcinka |AB|- punkty nie są współliniowe') else
begin
if (min(a.x,b.x)<=c.x)and(c.x<=max(a.x,b.x)) and (min(a.y,b.y)<=c.y)and(c.y<=max(a.y,b.y)) then
showmessage('Punkt C należy do odcinka |AB|') else
showmessage('Punkt C NIE należy do odcinka |AB|');
'''
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return not self.__eq__(other)

class Segment():
    def __init__(self,pt1,pt2):
        self.pt1 = pt1
        self.pt2 = pt2
        #self.pt1.x = 0
    def __contains__ (self, other):
        if isinstance (other ,Point):
            if orientation(self.pt1, self.pt2, other) != 0 :
                return False
            if(other.x <= max(self.pt1.x, self.pt2.x) and other . x >= min(self.pt1.x, self.pt2.x) and other.y <= max(self.pt1.y, self.pt2.y) and other.y >= min(self.pt1.y, self.pt2.y)) :
                return True
            else:
                return False
        else:
            raise ValueError ( "not a point" )

pt1 = Point(0,1)
pt2 = Point(3,4)
other = Point(2,2)

punkty = Segment(pt1,pt2)
print(other in punkty)

mass_file.close()
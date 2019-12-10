import string
password = []
for i in range(172930,683082):
    a, b, c = 0, 0, 0
    i = list(map(int, str(i)))
    if i[0]<=i[1]<=i[2]<=i[3]<=i[4]<=i[5]:
        a = 1
    if i[0]==i[1]!=i[2] or i[0]!=i[1]==i[2]!=i[3] or i[1]!=i[2]==i[3]!=i[4] or i[2]!=i[3]==i[4]!=i[5] or i[3]!=i[4]==i[5]:
        b = 1

    print(a,b)
    if a + b  == 2:
        password.append(i)
print(len(password))
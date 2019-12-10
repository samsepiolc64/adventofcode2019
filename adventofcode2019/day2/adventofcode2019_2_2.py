import math

path = 'data2.txt'
mass_file = open(path,'r')
for line in mass_file.readlines():
    data = line.rstrip().split(',')


def opcode(data):
    i = 0
    while i < len(data):
        instr = int(data[i])
        if instr == 1:
            data[int(data[i+3])] = int(data[int(data[i+1])])+int(data[int(data[i+2])])
        elif instr == 2:
            data[int(data[i+3])] = int(data[int(data[i+1])])*int(data[int(data[i+2])])
        elif instr == 99:
            pass
        else:
            pass

        i += 4
    return data[0]

for i in range(5,99):
    for j in range(5,99):
        d = data.copy()
        d[1]=str(i)
        d[2]=str(j)
        ss = opcode(d)
        print(ss)
        if ss == 19690720:
            print('-----------')

            odp = 100*int(d[1])+int(d[2])
            print(odp)


mass_file.close()
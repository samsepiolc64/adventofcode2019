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


ss = opcode(data)
print(ss)



mass_file.close()
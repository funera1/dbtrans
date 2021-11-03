valDict = dict()
with open('./vals.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        spl = line.split('=')
        valDict[spl[1]] = spl[0]

sepSet = set()
with open('./seps.txt') as f:
    for line in f:
        spl = line.split()
        for spi in spl:
            sepSet.add(spi)

#==========================================
def brankLine(str):
    res = ''
    for i in range(1, len(str)):
        pre = str[i - 1]
        nxt = str[i]

        res += pre
        if pre in sepSet:
            res += ' '
        elif nxt in sepSet:
            res += ' '
    res += str[-1]
    return res

def changeLine(str):
    spl = str.split(' ')
    for i in range(len(spl)):
        si = spl[i]
        if si in valDict.keys():
            spl[i] = valDict[si]
    res = ' '.join(spl)
    return res

def retLine(str):
    res = ''
    flag = False
    for i in range(1, len(str)):
        pre = str[i - 1]
        nxt = str[i]
        if flag:
            flag = False
            continue
        if pre in sepSet:
            flag = True
        if nxt in sepSet:
            continue
        res += pre
    res += str[-1]
    return res

print('input file path')
frompath = input()

strList = list()
with open(frompath, 'r') as f:
    for line in f:
        line = brankLine(line)
        line = changeLine(line)
        line = retLine(line)
        strList.append(str(line))
        # break
        
with open('return.txt', 'w') as f:
    for li in strList:
        f.write(li)

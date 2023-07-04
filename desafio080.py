numList = list()
numDig = 0
men = 0

for c in range(0, 5):
    numList.append(int(input(f'Digite o {c+1}º número: ')))

if numList[4] < numList[3]:
    men = numList[4]
    numList[4] = numList[3]
    numList[3] = men
if numList[4] < numList[0]:
    men = numList[4]
    numList[4] = numList[0]
    numList[3] = men
if numList[4] < numList[1]:
    men = numList[4]
    numList[4] = numList[1]
    numList[1] = men
if numList[4] < numList[2]:
    men = numList[4]
    numList[4] = numList[2]
    numList[2] = men

if numList[3] < numList[2]:
    men = numList[3]
    numList[3] = numList[2]
    numList[2] = men
if numList[3] < numList[1]:
    men = numList[3]
    numList[3] = numList[1]
    numList[1] = men
if numList[3] < numList[0]:
    men = numList[3]
    numList[3] = numList[0]
    numList[0] = men

if numList[2] < numList[1]:
    men = numList[2]
    numList[2] = numList[1]
    numList[1] = men
if numList[2] < numList[0]:
    men = numList[2]
    numList[2] = numList[0]
    numList[0] = men

if numList[1] < numList[0]:
    men = numList[1]
    numList[1] = numList[0]
    numList[0] = men

print(f'Esses foram os números digitados: {numList} ')
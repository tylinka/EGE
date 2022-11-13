a = [0] * 100
data = []
n = 15 # не забыть изменить

for i in range(n):
    t, p = input().split()
    data.append([i+1, int(t), list(map(int, p.split(';')))])

i = 0
while i < len(data):
    if data[i][2] == [0]:
        a[data[i][1]] = [data[i][0]]
        data.pop(i)
    else:
        i += 1

i = 0
while len(data) > 0:
    t = data[i][2]
    k = []
    for x in t:
        for j in range(len(a)): # поиск в списке a
            if a[j] != 0 and x in a[j]:
                k.append(j) # если нашли в списке а, то добавляем номер (время) в новый список
                break
    if len(k) == len(t): # если все процессы уже прошли
        p = max(k) + data[i][1]
        if a[p] == 0: # если это первый процесс в данном времени
            a[p] = [data[i][0]]
        else:
            a[p].append(data[i][0])
        data.pop(i)
    else:
        i += 1
        if i == len(data):
            i = 0

for i in range(len(a)-1, -1, -1):
    if a[i] != 0:
        print(f'Answer: {i}')
        break



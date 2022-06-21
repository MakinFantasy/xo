f = open('medium/24.txt').readline()


def most_frequent(List):
    return max(set(List), key=List.count)


k = []


for i in range(len(f)-1):
    if f[i] == 'A':
        k.append(f[i+1])
print(most_frequent(k))
print(max(set(k), key=k.count))

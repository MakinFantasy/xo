def most(n):
    return max(n, key=n.count)


with open('24kulab_1.txt') as f:
    s = f.readline()
    mas = []
    for i in range(len(s) - 2):
        if s[i+1] == 'A' and s[i+2] == 'D':
            mas.append(s[i])

print(most(mas), mas.count(most(mas)))
print(max(mas, key=mas.count), mas.count(max(mas, key=mas.count)))

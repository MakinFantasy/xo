# all - 100

with open('26A6.txt') as f:
    s = [int(i) for i in f]
    razn = max(s) - min(s)
    print(s)
    s.sort()
    print(s)
    min_mas = []
    max_mas = []
    for j in range(0, 10):
        min_mas.append(s[j])
    print(min_mas)
    s.reverse()
    print(s)
    for j in range(0, 10):
        max_mas.append(s[j])
    print(max_mas)
    min_sr = sum(min_mas) // 10
    max_sr = sum(max_mas) // 10
    result = max_sr // min_sr
    print(result, razn)
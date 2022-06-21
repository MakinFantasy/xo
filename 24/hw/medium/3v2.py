f=open("k7c-6.txt").readline()
counter=0
for i in range(len(f)-2):
    if f[i]!=f[i+1]!=f[i+2] and f[i]!=f[i+2]:
        counter+=1
print(counter)
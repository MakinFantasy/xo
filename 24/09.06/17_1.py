with open('17.txt') as f:
    s = f.readlines()
    arr = [int(num) for num in s]


def converttooctal(n):
    if n == 0:
        return 0
    octal = ''
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    octal = int(octal)

    return octal


print(arr)
mx = 0
k = 0
for i in arr:
    if converttooctal(i) % 10 == 7 and converttooctal(i) % 100 != 27:
        k += 1
        mx = max(i, mx)

print(k, mx)

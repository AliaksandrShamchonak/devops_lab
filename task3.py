n = int(input("Input number: "))
print("My value", n)

temp = n
out = []
numbers = set(range(2, 10))

c = 1
while temp != 1:
    for i in numbers:
        if temp % i == 0:
            c = i
            out.append(c)
            break
    else:
        print("-1")
        exit(0)
    temp /= c

out.reverse()
out2 = []

i = 0
while i < (len(out) - 1):
    if (out[i] * out[i + 1]) > 9:
        out2.append(out[i])
        i += 1
    else:
        out[i] = out[i] * out[i + 1]
        del out[i + 1]

out2.append(out[-1])
out2.sort()
for i in out2:
    print(i, end='')

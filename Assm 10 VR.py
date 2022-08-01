user = int(input("Enter the number of sequence you want!: "))
a = 2
b = 9
i =0
result = 0
for i in range (1, user+1):
    if i%2 ==0:
        n = -1
    else: n =1
    result = result + n * a / b
    a += 3
    b += 4
print(result)
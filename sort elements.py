start = 1
end = 15
for num in range (start, end +1):
    if num>1:
        for c in range (2, num):
            if (num % c==0):
                break
        else:
            print(num, end="")
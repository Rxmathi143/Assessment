def frequency(n):
    c = []
    if len(n) > 1:
        for i in range(len(n)-1):
            if len(a[i])<len(a[i+1]):
                c.append(i)

        c.sort()

        return(c[0])
    else:
        return a[0]






a = input().split(" ")
print(frequency(a))

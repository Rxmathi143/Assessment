def SecondLargest(arr):
    arr2 = []
    largest = max(arr)
            
    for i in arr:
        if i < largest:
            arr2.append(i)
    arr2.sort(reverse=True)
    second_largest = arr2[0]
    return second_largest

inp = input().split()

arr = list(map(int,inp))
count = 0
for i in inp:
    if len(i) == 1:
        count += 1

if count < 2:
    print(-1)
else:
    print(SecondLargest(arr))


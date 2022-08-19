n = 5
t = [1, 2, 3, 4, 5]

e = 2

start = 0
end = n-1
found = False
while start <= end and not found:
    mid = start + ((end - start) // 2)
    if t[mid] == e:
        found = True
    elif t[mid] < e:
        start = mid+1
    else:
        end = mid-1


print(found)


print(t)

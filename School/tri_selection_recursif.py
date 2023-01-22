def tri_selection_recursif(n, deb):
    global t
    posMin = deb
    for i in range(deb+1, n):
        if t[i] < t[posMin]:
            posMin = i
    if posMin != deb:
        aux = t[deb]
        t[deb] = t[posMin]
        t[posMin] = aux
    if deb < n-1:
        tri_selection_recursif(n, deb+1)


t = [3, 5, 1, 3, -1, 5]
tri_selection_recursif(6, 0)
print(t)

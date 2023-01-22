def tri_shaker(n):
  global t
  valid = False
  while not valid:
    permut = False
    for i in range(n-1):
      if t[i] > t[i+1]:
        aux = t[i]
        t[i] = t[i+1]
        t[i+1] = aux
        permut = True
      if t[n-1-i] < t[n-2-i]:
        aux = t[n-1-i]
        t[n-1-i] = t[n-2-i]
        t[n-2-i] = aux
        permut = True
    valid = permut == False


t = [5,4,1,2,3,0,-1,-2,5]
tri_shaker(len(t))
print(t)
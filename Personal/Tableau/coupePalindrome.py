def estPalindrome(T, n, i, j):
    flag = True
    k = 0
    v = False
    while not v:
        if T[i+k] != T[j-k]:
            flag = False
        k = k + 1
        v = (not flag) or (k == (j-i)//2 + 1)
    """
    # OTHERWISE

    flag = True
    k = -1
    v = False
    while not v:
        k = k + 1
        if T[i+k] != T[j-k]:
            flag = False
        v = (not flag) or (k == (j-i)//2)
    
    """
    return flag


T = [14, 7, 9, -4, 8, 5, 1, 5, 8, -4, -9, 25]

if estPalindrome(T, len(T), 3, 9):
    print("Cette coupe est un palindrome.")
else:
    print("Cette coupe n'est pas un palindrome.")

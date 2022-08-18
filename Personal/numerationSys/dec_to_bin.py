def dec_to_bin(n):
    ch = ""
    while n != 0:
        ch = str(n % 2) + ch
        n = n // 2
    return ch


print(dec_to_bin(7))
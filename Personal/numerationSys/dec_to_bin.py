def dec_to_bin(n):
    ch = ""
    while n != 0:
        ch = str(n % 2) + ch
        n = n // 2
    return ch


print(dec_to_bin(8))






# def dec_to_bin(n):
#     ord = 0
#     bin = 0
#     while n != 0:
#         reste = n % 2
#         puissance = 10 ** ord
#         bin = bin + reste * puissance
#         ord = ord + 1
#         n = n // 2
#     return bin
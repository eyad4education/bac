def decimal_to_bin(N):
    bin = ""
    while N != 0:
        bin = str(N % 2) + bin
        N = N // 2
    if len(bin) == 1:
        return "00" + bin
    elif len(bin) == 2:
        return "0" + bin
    else:
        return bin


def octale_to_bin(oct):
    T = [str()] * 8
    for i in range(8):
        T[i] = decimal_to_bin(i)
    bin = ""
    for i in range(len(oct)):
        bin = bin + T[int(oct[i])]
    return bin


print(octale_to_bin("524"))

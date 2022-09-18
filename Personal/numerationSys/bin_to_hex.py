def bin_hex(ch):
    if len(ch) % 4 > 0:
        for i in range(4 - len(ch) % 4):
            ch = "0" + ch
    hexa = ""
    for j in range(len(ch) // 4):
        nb = 0
        ch1 = ch[0:4]
        for i in range(len(ch1)):
            nb = nb + int(ch1[i]) * (2**(len(ch1)-i-1))
        if nb > 9:
            hexa = hexa + chr(nb + 55)
        else:
            hexa = hexa + str(nb)
        ch = ch[4:len(ch)]
    return hexa


print(bin_hex("1011100011"))

# RESULT = 2E3

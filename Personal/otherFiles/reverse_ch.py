def reverse1(ch):
    if ch == "":
        return ""
    return ch[len(ch)-1:len(ch)] + reverse(ch[0:len(ch)-1])

def reverse2(ch):
    if ch == "":
        return ""
    return reverse2(ch[1:len(ch)]) + ch[0]

print(reverse2("abcd"))
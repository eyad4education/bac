def chainePalindrome(ch):
    ch1 = ""
    for i in range(len(ch)):
        ch1 = ch1 + ch[len(ch)-i-1]
    if ch1 == ch:
        return True
    else:
        return False


T = ["kayak", "deified", "rotator", "repaper",
     "wow", "not", "test", "kinda", "simple"]
for i in range(len(T)):
    if chainePalindrome(T[i]):
        print(f"Cette chaine \"{T[i]}\" est un Palindrome.")
    else:
        print(f"Cette chaine \"{T[i]}\" n'est pas un Palindrome.")

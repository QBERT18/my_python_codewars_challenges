def swap(s, n):
    n = format(n, "b")
    nArray = []
    newS = ""
    while len(nArray) < len(s):
        for x in n:
            nArray.append(x)
    for i in range(0, len(s)):
        if not s[i].isalpha():
            nArray.insert(i, "x")
    while len(nArray) > len(s):
        nArray = nArray[0:-1]
    for i in range(0, len(s)):
        if s[i].isalpha() and nArray[i] == '1':
            if s[i].isupper():
                newS += s[i].lower()
            else:
                newS += s[i].upper()
        else:
            newS += s[i]
    return newS
def isAnagram(s1, s2):
    if(len(s1)!=len(s2)):
        return False
    
    s1.lower()
    s2.lower()
    
    letters=[0]*26
    for c in range(len(s1)):
        letters[c]=letters[c]+1

    for c in range(len(s2)):
        letters[c]=letters[c]-1

    for i in letters:
        if i!=0:
            return False
    
    return True

print(isAnagram("aba","bbaa"))
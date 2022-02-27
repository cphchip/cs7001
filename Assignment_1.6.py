userVal = str(input("Enter the letter: "))

def is_vowel(n1:chr) -> bool:
    vList = ['a', 'e', 'i', 'o', 'u']
    for x in vList:
        if x == n1:
            return True
    return False

print (is_vowel(userVal))

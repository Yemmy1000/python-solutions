def replaceVowels(strg):
    reStr = ""
    for letter in strg:
        if letter in "aeiou":
            iletter = letter.upper()
        else:
            iletter = letter
        
        reStr += iletter    
    return reStr  

def main():
    strg = input("Enter string ")
    print("Replaced vowels: ", replaceVowels(strg))

main()


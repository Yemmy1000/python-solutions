def countVowels(strg):
    count = 0
    for letter in strg:
        if letter in "aeiou":
            count += 1
    return count  

def main():
    strg = input("Enter string ")
    strg = strg.lower()
    print("Number of vowels is: ", countVowels(strg))

main()

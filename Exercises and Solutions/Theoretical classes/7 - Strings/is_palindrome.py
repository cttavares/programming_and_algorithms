pal = "abba"
non_pal = "anda"

def e_palindrome (word):
    pos = 0
    palindrome = True
    print ("Word: ", word)   
    while pos <= (len (word)//2) - 1:
        if word [pos] != word [-1-pos]:
            palindrome = False
            break
        pos = pos + 1

    return palindrome

print ("A palavra ",pal, " é palindrome:", e_palindrome (pal))
print ("A palavra ",non_pal, " é palindrome:", e_palindrome (non_pal))
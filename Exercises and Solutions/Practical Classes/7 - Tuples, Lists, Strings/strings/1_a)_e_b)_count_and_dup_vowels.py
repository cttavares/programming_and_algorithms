s = "Something extraordinary"

def is_vowel (s):
    if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
        return True

count = len ([i for i  in filter (is_vowel, s.lower())])
print ("Number of vowels is: ", count)

i = 0
final = ""
while i < len (s):
    if is_vowel (s [i].lower()):
        final += s [i]
        final += s [i]
        final += s [i]
    else:
        final += s[i]
    
    i = i + 1

print ("String with triplicated: ", final)
str = "abbbaabbaa"
dup = "b"
nov = ""

for i in str:
    if i not in dup:
        nov = nov + i
    else:
        nov = nov + i*2

print (nov)

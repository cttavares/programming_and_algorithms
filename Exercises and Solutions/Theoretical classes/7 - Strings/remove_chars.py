str = "abbaabbaabba"
rem = "b"

nova = ""

for i in str:
    if i not in rem:
        nova = nova + i

print (nova)
str = "abbaabbaabba"
dup = "b"

res = ""
for i in str:
    if i in dup:
        res = res + i*2
    else:
        res = res + i

print (res)

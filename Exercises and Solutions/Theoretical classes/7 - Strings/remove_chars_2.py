str = "abababababbababa"
to_rem = "b"
res = ""
for i in str:
    if i not in to_rem:
        res = res + i

print (res)

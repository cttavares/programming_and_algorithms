def factorial (n):
    assert n > 0, "Vai aprender sobre factoriais"
    if n < 2:
        return 1
    return n * factorial (n-1)

fact = factorial (-3)
print (fact)
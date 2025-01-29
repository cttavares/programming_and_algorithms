x = 30
assert x <= 40 and x >= 20, "Erro 1"

# Bloco
d1 = x // 100
d2 = x % 10
assert d2 == x % 10 and d1 == x // 10, "Erro no Bloco 2"

sum_1 = d1 + 1927
sum_2 = d2 + 1927
assert sum_1 == d1 + 1927 and sum_2 == d2 + 1927, "Erro 3"


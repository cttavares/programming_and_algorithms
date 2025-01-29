from functools import cache

# Uma funcao recursiva para o calculo de combinacoes
# implementacao directa da definicao dada.
@cache
def combinations (n, k):
    if k == 0:
        return 1
    if n == k:
        return 1
    return combinations (n-1, k-1) + combinations (n-1,k)

print ("Combinations: ", combinations (4, 2))
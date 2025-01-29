# Multiplies and sums every pair of numbers from 1 to 100 j=i=1
sum = 0
i = 1
j = 1
while i <= 100: 
    while j <= 100:
        sum = sum + (i*j)
        j = j + 1
    i = i + 1

print ("Sum and multiply: ", sum)
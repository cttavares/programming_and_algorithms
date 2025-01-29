tuple_list = []
# (copies, low, high)
tuple_list.append ((2, 0 ,2))
tuple_list.append ((3, 4, 8))
tuple_list.append ((7, 2, 5))

s = "JoseJoseJose"
res = ""
for i in tuple_list:
    (copies, low, end) = i
    res += s [:low] + s [low:end]*copies + s [end:]

print (res)
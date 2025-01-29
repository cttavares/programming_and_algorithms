t = ["truthy", "falsy", "falsy", "falsy", "truthy"]

for i in map (lambda x: True if x == "truthy" else False, t):
    print (i)
d = dict ()

# Creation consists in just using the key
d ["some_key"] = "Some_element"

print (d)

# Change, just use the key again
d ["some_key"] = "Another element"
print (d)

# To remove use the pop function
d.pop("some_key")
print (d)
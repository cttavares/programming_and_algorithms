try:
    x = int (input ("Write a number: "))
    y = 1/x
    print ("Y: ", y)
except ZeroDivisionError:
    print("This was division by zero")
except:
    print("This was some unknown error")
else:
    print("No error!")
finally:
    print("This will always be executed!")
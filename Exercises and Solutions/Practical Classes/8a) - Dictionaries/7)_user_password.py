d = {"as312": "amordemae", "as123": "1asdaswe", "as234": "password"}

def verify (user, password):
    if d [user] == password:
        print ("Correct!")
    else:
        print ("Not correct!")


user_1 = "as234"
password_1 = "password"

user_2 = "as312"
password_2 = "sporting02"

verify (user_1, password_1)
verify (user_2, password_2)
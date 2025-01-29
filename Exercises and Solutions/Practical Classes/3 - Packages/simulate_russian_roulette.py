import random

chambers = [0, 0, 0, 0, 0, 1]
random.shuffle(chambers)

if chambers[0] == 1:
    print("Bang! You lost!")
else:
    print("Click! You're safe!")

consumption_rate = float (input ("Write the consumption rate(liters/hour): "))
speed = float (input ("Write the speed(knots/hour): "))
fuel_on_board = float (input ("Write the fuel on board(liters): "))

range = (fuel_on_board/consumption_rate)*speed
endurance = fuel_on_board/consumption_rate

print ("The range is: (knots)", range)
print ("The endurance is (hours): ", endurance)


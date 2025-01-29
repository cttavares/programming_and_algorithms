distance = float (input ("Write distance in km: "))
fuel = float (input ("Write fuel consumed: "))

fuel = fuel*0.264172
distance = distance*0.621371

fuel_effiency = fuel/distance
print ("Fuel efficiency: ", fuel_effiency)
def calculate_mach(TAS, altitude):
    # Constants
    gamma = 1.4  # Specific heat ratio
    R = 287  # Specific gas constant for dry air
    
    # Temperature using the ISA model (only valid up to 11,000m)
    if altitude <= 11000:
        T = 288.15 - 0.0065 * altitude
    else:
        T = 216.65  # Assumed constant temperature above 11,000m

    # Compute the Mach number
    Mach = TAS / (gamma * R * T)**0.5
    
    return Mach

# Get user input
TAS = float(input("Enter TAS in meters per second: "))
altitude = float(input("Enter altitude in meters: "))

# Calculate and display Mach number
Mach = calculate_mach(TAS, altitude)
print("The Mach number at an altitude of", altitude, "meters is:", Mach)

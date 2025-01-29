from datetime import datetime

# Get the current datetime
current_datetime = datetime.now()

# Extract and format the milliseconds
milliseconds = current_datetime.strftime("%f")[:3]

print(milliseconds)


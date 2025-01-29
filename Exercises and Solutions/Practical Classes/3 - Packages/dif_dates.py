from datetime import datetime

date_format = "%d/%m/%Y"
date1 = datetime.strptime("23/1/2023", date_format)
date2 = datetime.strptime("1/1/2023", date_format)

difference = (date1 - date2).days
print(difference)

from datetime import datetime

date_format = "%d/%m/%Y"

birth_date_str = input("Enter your birth date (dd/mm/yyyy): ")
birth_date = datetime.strptime(birth_date_str, date_format)

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
birth_day = days_of_week[birth_date.weekday()]

print("You were born on a ", birth_day)

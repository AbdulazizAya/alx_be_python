from datetime import datetime,timedelta

def display_current_datetime():
    return datetime.today().replace(microsecond=0)

current_date = display_current_datetime()
print(f"Current date and time: {current_date}")

number_of_days = int(input("Enter the number of days to add to the current date: "))
future_date = current_date + timedelta(days = number_of_days)
print(f"Future date: {future_date}")
from datetime import datetime,timedelta

def display_current_datetime():
    return datetime.now()

current_date = display_current_datetime().replace(microsecond=0)
print(f"Current date and time: {current_date}")

number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date (number_of_days):
    return current_date + timedelta(days = number_of_days)

future_date = calculate_future_date(number_of_days)
print(f"Future date: {future_date}")
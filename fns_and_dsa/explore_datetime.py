from datetime import datetime, timedelta

def display_current_datetime():
    return datetime.now()

current_date = display_current_datetime().replace(microsecond=0)
formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {formatted_current_date}")

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(days):
    return current_date + timedelta(days=days)

future_date = calculate_future_date(number_of_days)
formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
print(f"Future date: {formatted_future_date}")

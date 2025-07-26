from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    current_date = f"Current date and time: {current_date}"
    return  current_date

print(display_current_datetime())

num = input("Enter the number of days to add to the current date: ")
num = int(num)

def calculate_future_date():
    today = datetime.now().date()
    future_date = today + timedelta(days=num)
    future_date = f"Future date: {future_date}" 
    return future_date

print(calculate_future_date())
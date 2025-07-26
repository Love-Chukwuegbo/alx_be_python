from datetime import datetime , timedelta, date
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time: ",datetime.strftime(current_date, "%Y-%m-%d %H:%M:%S"))

display_current_datetime()
num_of_days = int(input("Enter the number of days to add to the current date:"))

def calculate_future_date():
    future_date= datetime.now() + timedelta(days=num_of_days)
    print("Future date: ", future_date.strftime("%Y-%m-%d"))
calculate_future_date()


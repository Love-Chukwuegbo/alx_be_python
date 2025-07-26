import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current date and time: ", datetime.datetime.isoformat(current_date))

display_current_datetime()
num_of_days = int(input("Enter the number of days to add to the current date:"))

def calculate_future_date():
    future_date= datetime.datetime.now() + datetime.timedelta(days=num_of_days)
    print("Future date: ", datetime.date.isoformat(future_date))
calculate_future_date()


# This is Lab 3 - Calculate number of days in 2023

# Import calendar
import calendar

# User to enter desired year.
year = int(input("Enter year: "))

# Define function to determine days.
def num_days_in_year(year) :
    return 365 + calendar.isleap(year)

# Print number of days of year inputted by user.
print(f"Hello, there are", str(num_days_in_year(year))+ " days in " + str(year)+ ".")

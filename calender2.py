import calendar


def print_calendar():
    year = int(input("Enter the year: "))
    month_input = input("Enter the month (name or number): ")

    # Convert month input to integer if it's a number
    if month_input.isdigit():
        month = int(month_input)
    else:
        month = list(calendar.month_name).index(month_input.capitalize())

    # Print the calendar
    print(f"The calender for the month of {calendar.month_name[month]} is: ")
    print(calendar.month(year, month))


print_calendar()

import calendar

year = int(input("Enter the year:  "))
# month = input("Enter the month:  ")
# print(calendar.month(year, month))


print(f"The calender for the year {year} is as follows: ")
print(calendar.calendar(year))

# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order,
#  formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date = input("Introduce date: ")

if date[0].isdigit():
    month, day, year = date.split("/")
    print(f"{year}/{month:02}/{day:02}")



elif date[0].isalpha():
    month, day, year = date.split(" ")
    month = month.title()
    month = months.index(month)+1
    day = int(day.replace(",",""))
    print(f"{year}/{month:02}/{day:02}")


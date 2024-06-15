# Calendar Month Display

This is a simple Python script to display the calendar for a given month and year.

## Description

The script defines a function `date` which takes a year and a month as arguments and prints the calendar for that month using Python's built-in `calendar` module. The script prompts the user to input the year and month, and then uses the `date` function to display the calendar.

## Code

```python
import calendar

def date(year, month):
  print(calendar.month(int(year), int(month)))

year = input("Enter year: ")
month = input("Enter month: ")

date(year, month)

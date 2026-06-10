days=int(input('Enter the value for days::'))
year=days//365
remaining_days=days%365
weeks=remaining_days//7
day=remaining_days%7
print("reamaining days are::",remaining_days)
print("year is::",year)
print("week is::",weeks)
print("days are::",day)
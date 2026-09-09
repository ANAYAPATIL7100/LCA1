import re
text = input("Enter a string:")
if re.fullmatch(r'[A-Za-z0-9]+', text):
    print("The string contains only letters and numbers.")
else:
    print("The string contains characters other than letters and numbers.")
    
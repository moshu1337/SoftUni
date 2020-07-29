import re
text = input()
pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"
dates = re.findall(pattern, text)

for date in dates:
    print(f"Day: {dates[0]}, Month: {dates[2]}, Year: {dates[3]}")
# the 1 index of dates is the separator


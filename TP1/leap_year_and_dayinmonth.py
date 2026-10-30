# a

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# b

def days_in_month(month, year):
    if month < 1 or month > 12:
        return None
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31

# c
for i in (1900, 2000, 2024, 2026):
    print(i, "leap" if is_leap(i) else "not leap")
    
# Month example:
print(
    f"Feb 2024: {days_in_month(2, 2024)} | "
    f"Feb 2026: {days_in_month(2, 2026)} | "
    f"Apr : {days_in_month(4, 2026)} | "
    f"month 13: {days_in_month(13, 2026)}"
)


# d
count = 0
for i in range(2000, 2100):
    if is_leap(i):
        count += 1
print("Leap years from 2000 to 2100: ", count)
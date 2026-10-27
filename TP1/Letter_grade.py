def letter_grade(score):
    if score < 0:
        return "Invalid"
    elif score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    elif score < 96:
        return "A"
    elif score > 100:
        return "Invalid"
    else:
        return "A+"


# a
scores = [99, 90, 85.5, 72, 60, 59.9, -5, 101]

for i in scores:
    print(f"{i} -> {letter_grade(i)}")
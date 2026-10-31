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
    
# Why A+ must come before A:

# An if / elif / else chain is checked from top to bottom, and Python runs only the first branch whose condition is true. The remaining branches are skipped. Because the conditions overlap (every score that is >= 97 is also >= 90), the order decides which branch wins.

# What happens if you swap them:

# A score of 99 satisfies score >= 90, so the function returns "A" immediately. The score >= 97 branch can never be reached, because any score that would satisfy it has already been caught by the >= 90 test. The result is that 99 -> A instead of 99 -> A+, and no error is raised. That makes it a logic bug that is easy to miss.
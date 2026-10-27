# a

def describe(*numbers, decimals = 2, label = "Data"):
    if not numbers:
        print(f"{label}: no values ")
        return None
    count = len(numbers)
    lowest = min(numbers)
    highest = max(numbers)
    mean = round(sum(numbers)/count, decimals)
    print(f"{label}: n={count} min={lowest} max={highest} mean={mean}")
    return (count, lowest, highest, mean)
# b

def make_tag(text, **style):
    attrs = "".join(f'{key}="{value}"' for key, value in style.items())
    return f"<span {attrs}>{text}</span>"

# c
square = lambda x: x ** 2
is_adult = lambda age: age >= 18

# Testing code
describe(12, 7, 30, 4)
describe(3.14159, 2.71828, decimals=3, label="Constants")
describe()
print(make_tag("Hello", color="red", size=14 ))
print(square(9), is_adult(17), is_adult(21))
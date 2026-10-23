def celsius_to_fahrenheit(c, round_to = 1):
    f = c * 9/5 + 32
    
    return round(f, round_to)

def fahrenheit_to_celsius(f, round_to = 1):
    c = (f - 32) * 5/9
    
    return round(c, round_to)
    
    
# a
print("°C        |       °F")
print("______________________")
for c in range(0, 101, 20):
    print(f"{c :> 3} °C    | {celsius_to_fahrenheit(c)} °F")
   
# b 
c = fahrenheit_to_celsius(98.6)
print(f"{98.6} °F = {c} °C")
    
# c
f = celsius_to_fahrenheit(37)
back = fahrenheit_to_celsius(f)
print(f"{f} °F, {back} °C, {back == 37.0}")

# d
print(celsius_to_fahrenheit(36.6, round_to=3))
print(fahrenheit_to_celsius(100, round_to=3))



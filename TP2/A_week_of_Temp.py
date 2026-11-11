days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = [31, 33, 29, 34, 35, 32, 30]

print("Number of days:", len(temps))
print("First day:", days[0], temps[0])
print("Last day:", days[-1], temps[-1])

print("Highest:", max(temps))
print("Lowest:", min(temps))
average = sum(temps) / len(temps)
print("Average: ", round(average, 1))

hottest = temps.index(max(temps))
print(f"index of hottest temps: {hottest}")
print("Hottest day:", days[hottest])

print("Sorted :", sorted(temps))
print("Original:", temps)
print(temps.sort())
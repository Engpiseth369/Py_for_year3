# a

def electricity_bill(kwh):
    if kwh < 0:
        return None
    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)
    
    cost = tier1 * 480 + tier2 * 610 + tier3 * 730
    total = (cost + 2000) * 1.10
    return round(total)

# b
for kwh in (0, 35, 50, 120, 200, 350):
    bill = electricity_bill(kwh)
    usd = bill / 4100
    print(f"{kwh:>3} kwh -> {bill:>9,} riel (≈ {usd:>6.2f}) USD")
    
# c
kwh = float(input("Enter your monthly consumption(kwh): "))
bill = electricity_bill(kwh)

if bill is None:
    print("Consumption cannot be negative.")
else:
    print(f"Your bill: {bill:,} riel (≈ {bill/4100})")
    
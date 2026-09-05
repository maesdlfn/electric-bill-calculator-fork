# Barangay Electric Bill Calculator — REPORTED BROKEN, PLEASE FIX

name = input("Enter resident name: ")
consumption = int(input("Enter kWh consumed this month: "))
is_senior = input("Senior citizen? (yes/no): ")

if consumption <= 100:
    rate = 9.00
elif consumption < 200:
    rate = 11.00
else:
    rate = 14.00
total = consumption * rate

if is_senior == "yes":
    discount = total * 0.05
    total = total - discount
    print(f"Senior discount applied: ₱{str(discount)}")
    print("----- ELECTRIC BILL -----")
    print(f"Name: {name}")
    print(f"Consumption: {str(consumption)} kWh")
    print(f"Rate applied: ₱{str(rate)} /kWh")
    print(f"Total Due: ₱{str(total)}")
elif is_senior == "no":
    print("----- ELECTRIC BILL -----")
    print(f"Name: {name}")
    print(f"Consumption: {str(consumption)} kWh")
    print(f"Rate applied: ₱{str(rate)} /kWh")
    print(f"Total Due: ₱{str(total)}")
else:
    print("Invalid Choice!")


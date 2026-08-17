# First-Order Predicate Calculus

machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

for machine, status in machines.items():
    if status == "Active":
        print(f"Active({machine})")
        print(f"Producing({machine})")
    else:
        print(f"Maintenance({machine})")
        print(f"Not Producing({machine})")

# Product production
production = {
    "M1": "Gear",
    "M2": "Wheel",
    "M3": "Gear",
    "M4": "Bolt"
}

print("\nAvailable Products:")

for machine, product in production.items():
    if machines[machine] == "Active":
        print(product)

print("\nGear production:")
if machines["M3"] == "Maintenance":
    print("Gear production is affected by maintenance on M3.")

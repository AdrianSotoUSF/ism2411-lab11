# ISM2411 Lab 11 — Customer Dictionary & Lookup
# Adrian Soto


# EXERCISE 1: One customer
print("EXERCISE 1")
customer = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.75,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)
print()


# EXERCISE 2: Update and add
print("EXERCISE 2")
customer["phone"] = "813-555-0142"     # add a new field
print(customer)

customer["tier"] = "platinum"           # update an existing field
print(customer)

del customer["email"]                   # delete a field
print(customer)
print()


# EXERCISE 3: Safe lookup
print("EXERCISE 3")
email = customer.get("email", "no email on file")
print(f".get() result: {email}")

try:
    print(customer["email"])
except KeyError as error:
    print(f"Bracket lookup raised KeyError: {error}")
print()


# EXERCISE 4: Iterate
print("EXERCISE 4")
for key, value in customer.items():
    print(f"{key}: {value}")

print("Without .items():")
for key in customer:
    print(key)
# Looping over a dict by itself only gives the keys.
# .items() gives (key, value) pairs, so both can be printed without
# looking each value up again with customer[key].
print()


# EXERCISE 5: Lookup table
print("EXERCISE 5")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
purchase = 200
final_price = purchase * (1 - discount_rate)

print(f"Tier: {tier}")
print(f"Discount rate: {discount_rate:.0%}")
print(f"Final price on ${purchase}: ${final_price:.2f}")
print()


# EXERCISE 6: List of dicts
print("EXERCISE 6")
customers = [
    {"name": "Alice Johnson", "tier": "platinum", "ytd_spend": 1250.75},
    {"name": "Brian Lee", "tier": "silver", "ytd_spend": 430.00},
    {"name": "Carmen Diaz", "tier": "bronze", "ytd_spend": 95.50},
]

purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount = purchase * rate
    print(f"{c['name']} | Tier: {c['tier']} | Discount on ${purchase}: ${discount:.2f}")
print()


# EXERCISE 7: Nested catalog
print("EXERCISE 7")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} left")
print()


# EXERCISE 8: Sales by region
print("EXERCISE 8")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for t in transactions:
    region = t["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + t["amount"]

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")

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

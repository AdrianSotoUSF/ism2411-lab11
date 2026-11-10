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

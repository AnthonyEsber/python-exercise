people = {
    "Alice": {"age": 30, "city": "New York"},
    "Bob": {"age": 25, "city": "Los Angeles"},
    "Charlie": {"age": 35, "city": "Chicago"}
}

oldest_name = None
max_age = 0


for name, details in people.items():
    if details["age"] > max_age:
        max_age = details["age"]
        oldest_name = name

print(f"oldest: {oldest_name}, age: {max_age}")

new_yorkers = [name for name, details in people.items() if details["city"] == "New York"]

print(f"people in ny: {new_yorkers}")

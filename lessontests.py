""" fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit) """

""" word = "Python string"
for index, letter in enumerate(word):
    print(index, letter) """

""" days = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday"}
for index, key in enumerate(days):
    print(index, key, days[key]) # index = number, key = entry (ex. mon), days[key] = key of key (ex. monday) """

""" students = ["Alice", "Bob", "Charlie"]
indexed_students = [(i, student) for i, student in enumerate(students, start=1)]
print(indexed_students) """

""" numbers = [1, 2, 3, 4, 5]
# Use map() to double the numbers
doubled_numbers = map(lambda x: x * 2, numbers)
print(list(doubled_numbers)) """

""" data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row (skip this)
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]
for row in data[1:]:  # Skip the first row
    print(row) """

""" def calcRow(data):
    row_totals = {}
    for row in data[1:]:  # Skipping the first row
        store_name = row[0]  # First column is the store name
        sales = map(int, row[1:])  # Convert sales to numbers
        row_totals[store_name] = sum(sales)  # Sum up sales for the store
    return row_totals
# Example Data
sales_data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
] 
totals = calcRow(sales_data)
print(totals) """

""" def calcRowLC(data):
    row_totals = {row[0]: sum([int(x) for x in row[1:]]) for row in data[1:]}
    return row_totals
print(calcRowLC(sales_data)) """

# map final challenge
temperatures = ["Label", 32, 50, 77, 104]
converted = map(lambda x: (x - 32) * 5/9, temperatures[1:])
print(list(converted))

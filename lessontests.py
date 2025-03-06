""" fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit) """

""" word = "Python string"
for index, letter in enumerate(word):
    print(index, letter) """

""" days = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday"}
for index, key in enumerate(days):
    print(index, key, days[key]) # index = number, key = entry (ex. mon), days[key] = key of key (ex. monday) """

students = ["Alice", "Bob", "Charlie"]
indexed_students = [(i, student) for i, student in enumerate(students, start=1)]
print(indexed_students)
## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list

file_path = "SalesData.csv"  
data = csv_to_list(file_path)


# 1) 
""" avgs = []
for row in data[1:]:
    stores = row[0]
    sales = list(map(int, row[1:]))
    avg_sales = sum(sales) / len(sales)
    avgs.append((stores, avg_sales))
print(avgs) """

# 2) 
avgs = []
for row in data[1:]:
    stores = row[0]
    sales = list(map(int, row[1:]))
    avg_sales = sum(sales) / len(sales)
    avgs.append((stores, avg_sales))
print(sorted(avgs, key=lambda x:x[1], reverse = True))

# 3)
avgs = []
for row in data[1:]:
    sales = list(map(int, row[1:]))
    avg_sales = sum(sales) / len(sales)
    avgs.append(avg_sales)
for x in avgs:
    all_stores = sum(avgs) / len(avgs)
print(all_stores)

# 4) 
avgs = []
danger = []
below = 0
all_stores = 0
store_avg = []
for row in data[1:]:
    stores = row[0]
    sales = list(map(int, row[1:]))
    avg_sales = sum(sales) / len(sales)
    avgs.append(avg_sales)
    store_avg.append((stores, avg_sales))
all_stores = sum(avgs) / len(avgs)
below = all_stores * 0.8
print("AVERAGES")
print(avgs)
print(all_stores, below)
for stores, avg in store_avg:
    if avg < below:
        danger.append((stores, avg))
print(danger)
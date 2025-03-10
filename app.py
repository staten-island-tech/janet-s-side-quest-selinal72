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


avgs = []
for row in data[1:]:
    stores = row[0]
    sales = list(map(int, row[1:]))
    avg_sales = sum(sales) / len(sales)
    avgs.append((stores, avg_sales))
print(avgs)




    


import csv

def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary
def main():
    PRODUCT_NUM_INDEX = 0
    products_dict = read_dictionary('products.csv', PRODUCT_NUM_INDEX)
    print(products_dict)
    
    with open('request.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first line (column headings)
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            
            product = products_dict.get(product_number)
            if product:
                product_name = product[1]
                price = float(product[2])
                total_price = quantity * price
                print(f"Product: {product_name}\nQuantity: {quantity}\nPrice: {price}\nTotal Price: {total_price}\n")
            else:
                print(f"Product with number {product_number} not found.\n")

if __name__ == '__main__':
    main()

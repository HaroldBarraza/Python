
import csv

def read_dictionary(filename, key_column_index):
    with open("products.csv", 'r') as filename:
        reader = csv.reader(filename)
        header = next(reader)
        products_dict = {}
        for row in reader:
            key = row[key_column_index]
            value = {header[i]: row[i] for i in range(len(header))}
            products_dict[key] = value
        return products_dict

def main():
    products_dict = read_dictionary('products.csv', 0)

    with open('request.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product_number = row['product_number']
            quantity = int(row['quantity'])
            if product_number in products_dict:
                product = products_dict[product_number]
                print(f"{product['name']} x {quantity} = ${float(product['price'])*quantity:.2f}")
            else:
                print(f"Error: Product {product_number} not found in products_dict")

if __name__ == "__main__":
    main()
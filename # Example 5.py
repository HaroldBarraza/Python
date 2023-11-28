import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary

def main():
    PRODUCT_NUM_INDEX = 0
    products_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)
    
    store_name = "Your Store"  # Update with your store name
    print(f"Store: {store_name}\n")

    ordered_items = []
    subtotal = 0

    with open('request.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            
            product = products_dict.get(product_number)
            if product:
                product_name = product[1]
                price = float(product[2])
                total_price = quantity * price
                subtotal += total_price

                ordered_items.append({
                    "Product": product_name,
                    "Quantity": quantity,
                    "Price": price,
                    "Total Price": total_price
                })

    # Print ordered items
    print("Ordered Items:")
    for item in ordered_items:
        print(f"Product: {item['Product']}")
        print(f"Quantity: {item['Quantity']}")
        print(f"Price: {item['Price']}")
        print(f"Total Price: {item['Total Price']}\n")

    # Print number of ordered items
    num_items = sum(item['Quantity'] for item in ordered_items)
    print(f"Number of Ordered Items: {num_items}\n")

    # Print subtotal
    print(f"Subtotal: {subtotal}\n")

    # Calculate and print sales tax
    tax_rate = 0.06  # 6% sales tax rate
    tax_amount = subtotal * tax_rate
    print(f"Sales Tax: {tax_amount}\n")

    # Calculate and print total amount due
    total_amount = subtotal + tax_amount
    print(f"Total Amount Due: {total_amount}\n")

    # Print thank you message
    print("Thank you for your purchase!\n")

    # Get current date and time
    current_datetime = datetime.now()
    print(f"Date and Time: {current_datetime}")

if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except KeyError:
        print("Error: Key not found.")
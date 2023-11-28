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
    try:
        PRODUCT_NUM_INDEX = 0
        products_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)

        store_name = "Inkom Emporium"
        print(f"Store: {store_name}\n")

        ordered_items = []
        subtotal = 0

        with open('request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                product = products_dict[product_number]
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

        print("Ordered Items:")
        for item in ordered_items:
            print(f"{item['Product']}: {item['Quantity']} @ {item['Price']}")

        num_items = sum(item['Quantity'] for item in ordered_items)
        print(f"Number of Ordered Items: {num_items}")
        print(f"Subtotal: {subtotal:.2f}")

        tax_rate = 0.06
        tax_amount = subtotal * tax_rate
        print(f"Sales Tax: {tax_amount:.2f}")

        total_amount = subtotal + tax_amount
        print(f"Total Amount Due: {total_amount:.2f}\n")

        print("Thank you for shopping at the Inkom Emporium.\n")

        current_datetime = datetime.now()
        print(f"Date and Time: {current_datetime.strftime('%a %b %d %H:%M %Y')}")

    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except PermissionError:
        print("Error: Permission denied.")
    except KeyError:
        print("Error: Unknown product ID in the request.csv file.")

if __name__ == '__main__':
    main()

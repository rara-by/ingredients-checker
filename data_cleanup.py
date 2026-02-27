import csv 

def data_cleanup():
    issues = 0

    # Duplicate product entries
    product_names = []
    with open("product_names.csv", 'r', newline='') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            product_names.append(row[0])

    duplicates = []
    for item in product_names:
        if product_names.count(item) > 1 and item not in duplicates:
            duplicates.append(item)

    if duplicates:
        print("Duplicates present!: ", duplicates)
        issues += 1
    else:
        print("No duplicates.")

    # Check for line breaks in the product_data.csv file
    # They occur due to formatting

    last_checked_line = 102

    with open("product_names.csv", 'r', newline='') as f:
        csv_reader = csv.reader(f)
        names_count = sum(1 for row in csv_reader)

    with open("product_data.csv", 'r', newline='') as f:
        csv_reader = csv.reader(f)
        data_count = sum(1 for row in csv_reader)

    if names_count == data_count:
        print("No new line breaks!")
    else:
        print("Check for a line break after line", last_checked_line,
            "in the product_data.csv file.")
        issues += 1

    return issues
import csv
from web_search import fetch_data 

def save_product_data(product_name, label):
    product_data = fetch_data(search_term=product_name) #="celimax dual")
    
    if not product_data:
        print("Please try again.")
        return

    # check if label is in correct format
    label = str.lower(label)
    print("Label: ", label)

    if label not in ['good', 'bad']:
        print('Label must be "good" or "bad".')
        return
    
    product_name = [product_data[0]]
    stored_product_names = []

    # save product names in a csv file if they aren't already recorded
    try:
        with open("product_names.csv", newline='') as names: # newline='' prevents extra blank rows
            reader = csv.reader(names, delimiter=',')
            for row in reader:
                if row:
                    stored_product_names.append(row)
            names.close()
    except FileNotFoundError:
            pass
            
    if product_name not in stored_product_names:
        with open("product_names.csv", 'a', newline='') as names: 
            writer = csv.writer(names, delimiter=',')
            writer.writerow(product_name)
            names.close()

        #write all product data in a csv file with product name, ingredients list and label in each row
        with open("product_data.csv", 'a', newline='') as data:
            writer = csv.writer(data, delimiter=',')
            writer.writerow(product_data + [label])
            data.close()
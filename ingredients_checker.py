from save_csv import save_product_data 

# url="https://incidecoder.com/"

product_list = []
product_data = []
good_ingredients = ()
bad_ingredients = ()

def main():

    product_name = input("Please input the product name: ")
    label = input("Was this product good or bad for your skin?: ") 
    save_product_data(product_name, label)
    

if __name__ == "__main__":
    main()
        
            

import csv
from web_search import fetch_data 
from data_cleanup import data_cleanup
from collections import Counter

def save_product_data(product_name, label):

    """ 
    This function saves product names and product data (ingredients, good or bad verdict)
    in two csv files.
    """

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
        print("Product list updated.")

    else:
        print("Product already listed, not updated.")


    

def save_ingredients_data():
    '''
    - Check for duplicates and formatting changes using the data_cleanup.py script.
    - Check for repeated ingredients listed differently.There is no naming convention for ingredients 
    so a single imgredient can be listed multiple times.
    - Save data for visualization and insights.
     '''
    
    issues = data_cleanup()
    # print(issues) 
    # if there are duplicates or formatting issues fix those first
    if issues:
        print("Please fix before proceeding.")
        return

    products = {} # dict format { product name: [Ingredients] }
    # storing good and bad product names and ingredients list only
    good_products = [] 
    bad_products = []
    all_good_ingredients = []
    all_bad_ingredients = []
    all_good_ingredients_set = set()
    all_bad_ingredients_set = set()

    with open("product_data.csv", 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile) #created a csv.reader object

        for row in csv_reader:
            if not row:
                continue
            products[row[0]] = row[1:]


    for key,val in products.items():
        products[key] = [str.lower(item) for item in val] # make product names lowercase


        if val[-1] == "good":
            good_products.append([key, val[:-1]])
            all_good_ingredients.extend(val[:-1])
            all_good_ingredients_set.update(val[:-1])
            all_good_ingredients_set.discard("1") # remove without raising error if it doesn't exist

        else:
            bad_products.append([key, val[:-1]])
            all_bad_ingredients.extend(val[:-1])
            all_bad_ingredients_set.update(val[:-1])
            all_bad_ingredients_set.discard("1") # remove without raising error if it doesn't exist

    all_ingredients_set = all_bad_ingredients_set | all_good_ingredients_set # union

    # replace the repeated ingredients listed/spelled differently
    # format {'ingredient to be replaced': 'ingredient to replace'}

    replace_dict = {' *aloe barbadensis leaf extract': 'aloe barbadensis leaf extract',
                    ' aloe barbadensis leaf extract': 'aloe barbadensis leaf extract',
                    ' aqua (water)': 'water',
                    ' water': 'water',
                    ' aqua(water)': 'water',
                    'aqua': ' water',
                    ' water (aqua)': 'water',
                    ' water(aqua/eau)': 'water',
                    ' water/aqua/eau': 'water',
                    ' tremella mushroom extract': 'tremella fuciformis (mushroom) extract',
                    'tremella fuciformis extract': 'tremella fuciformis (mushroom) extract',
                    ' tremella fuciformis (mushroom) extract': 'tremella fuciformis (mushroom) extract',
                    'anona cherimolia fruit extract': 'anthemis nobilis (chamomile) flower oil',
                    'aqua (water)': 'water',
                    'aqua(water)': 'water',
                    'aronia melanocarpa Fruit Extract': 'aronia melanocarpa (black chokeberry) fruit extract',
                    'bees wax': 'beeswax',
                    'brassica oleracea italica extract': 'brassica oleracea italica (broccoli) extract',
                    'camellia sinensis leaf extract': 'camellia sinensis (green tea) leaf extract',
                    '*camellia sinensis leaf ext': 'camellia sinensis (green tea) leaf extract',
                    'cucumis sativus fruit extract': 'cucumis sativus (cucumber) fruit extract',
                    'curcuma longa turmeric root extract': 'curcuma longa (turmeric) root extract',
                    'euterpe oleracea fruit extract': 'euterpe oleracea (acai) fruit extract',
                    'fragrance(parfum)': 'fragrance (parfum)',
                    'fragrance': 'fragrance (parfum)',
                    'fragrance/parfum': 'fragrance (parfum)',
                    'ginkgo biloba leaf extract': 'ginkgo biloba (ginkgo) leaf extract',
                    'glycyrrhiza glabra root extract': 'glycyrrhiza glabra (licorice) root extract',
                    'honey / mel / miel': 'honey',
                    'hydrogenated poly(c6-14 olefin)': 'hydrogenated poly (c6-14 olefin)',
                    'morus alba fruit extract': 'morus alba (white mulberry) fruit extract',
                    'olea europaea fruit oil': 'olea europaea (olive) fruit oil',
                    'oryza sativa bran oil': 'oryza sativa (rice) bran oil',
                    'pelargonium graveolens flower oil': 'pelargonium graveolens (geranium) flower oil',
                    'polygonum cuspidatum root extract': 'polygonum cuspidatum (japanese knotweed) root extract',
                    'rosa damascena flower oil': 'rosa damascena (rose) flower oil',
                    'rosmarinus officinalis leaf extract': 'rosmarinus officinalis (rosemary) extract',
                    'saccharum officinarum (sugar cane) extract': 'saccharum officinarum (sugarcane) extract',
                    'sugar cane extract': 'saccharum officinarum (sugarcane) extract',
                    'sambucus nigra fruit extract': 'sambucus nigra (elder) fruit extract',
                    'schisandra chinensis fruit extract': 'schisandra chinensis (schizandra berry) fruit extract',
                    'scutellaria baicalensis root extract': 'scutellaria baicalensis (baikal skullcap) root extract',
                    'simmondsia chinensis seed oil': 'simmondsia chinensis (jojoba) seed oil',
                    'sunflower seed oil': 'helianthus annuus (sunflower) seed oil',
                    'strawberry fruit extract': 'fragaria chiloensis (strawberry) fruit extract',
                    'tea tree leaf oil': 'melaleuca alternifolia (tea tree) leaf oil',
                    'theobroma cacao(cocoa) extract': 'theobroma cacao (cocoa) extract',
                    'tocopherol': 'tocopherol (vitamin e)',
                    'vitamin e': 'tocopherol (vitamin e)',
                    ' bifida ferment lysate': 'bifida ferment lysate',
                    ' cetyl ethylhexanoate': 'cetyl ethylhexanoate',
                    ' houttuynia cordata extract': 'houttuynia cordata extract',
                    ' panax ginseng root extract': 'panax ginseng root extract',
                    ' propolis extract': 'propolis extract',
                    ' snail secretion filtrate': 'snail secretion filtrate',
                    '[hyaluronic acid]': 'hyaluronic acid',
                    }

    def remove_duplicates_set(ingredients_set, replace_dict):

        temp = []
        for item in ingredients_set:
            if item in replace_dict.keys():
                temp.append(replace_dict[item])
                # print(item)
        
        # print("length before: ", len(ingredients_set))
        # print("temp length: ", len(temp))

        ingredients_set.update(temp)
        ingredients_set = ingredients_set - set(replace_dict.keys())
        # print("length after: ", len(ingredients_set))
        return ingredients_set
    
    all_bad_ingredients_set = remove_duplicates_set(all_bad_ingredients_set, replace_dict)
    all_good_ingredients_set = remove_duplicates_set(all_good_ingredients_set, replace_dict)
    all_ingredients_set = remove_duplicates_set(all_ingredients_set, replace_dict)

    common_ingredients_set = all_bad_ingredients_set & all_good_ingredients_set # intersection

    print("Updated all bad ingredients number: ", len(all_bad_ingredients_set))
    print("Updated all good ingredients number: ", len(all_good_ingredients_set))
    print("Updated all ingredients number: ", len(all_ingredients_set))
    print("Updated common ingredients number: ", len(common_ingredients_set))

    # List of ingredients including duplicates
    print("Total number of good ingredients: ", len(all_good_ingredients))
    print("Total number of bad ingredients: ", len(all_bad_ingredients))

    # Use replace_dict to  format same ingredients under different names into one
    all_good_ingredients_new = [replace_dict[ing] if ing in replace_dict.keys() else ing for ing in all_good_ingredients]
    all_bad_ingredients_new = [replace_dict[ing] if ing in replace_dict.keys() else ing for ing in all_bad_ingredients]

    # Record frequency of ingredients in a dict
    good_ingredients_frequency = Counter(all_good_ingredients_new)
    bad_ingredients_frequency = Counter(all_bad_ingredients_new)

    # complete save the data in  a csv
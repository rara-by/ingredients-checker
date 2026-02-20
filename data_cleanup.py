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


    
    # products = {}
    # good_products = [] 
    # bad_products = []
    # all_good_ingredients = []
    # all_bad_ingredients = []
    # all_good_ingredients_set = set()
    # all_bad_ingredients_set = set()

    # with open("product_data.csv", 'r', newline='') as csvfile:
    #     csv_reader = csv.reader(csvfile) #created a csv.reader object

    #     for row in csv_reader:
    #         if not row:
    #             continue
    #         products[row[0]] = row[1:]

    # for key,val in products.items():
    #     products[key] = [str.lower(item) for item in val] # make product name lowercase

    # for key,val in products.items():
    #     if val[-1] == "good":
    #         good_products.append([key, val[:-1]])
    #         all_good_ingredients.append(val[:-1])
    #         all_good_ingredients_set.update(val[:-1])
    #         all_good_ingredients_set.discard("1") # remove without raising error if it doesn't exist
    
    #     else:
    #         bad_products.append([key, val[:-1]])
    #         all_bad_ingredients.append(val[:-1])
    #         all_bad_ingredients_set.update(val[:-1])
    #         all_bad_ingredients_set.discard("1") # remove without raising error if it doesn't exist

    # all_ingredients_set = all_bad_ingredients_set | all_good_ingredients_set # union

    # # replace the repeated ingredients listed/spelled differently
    # # format {'ingredient to be replaced': 'ingredient to replace'}

    # replace_dict = {' *aloe barbadensis leaf extract': 'aloe barbadensis leaf extract',
    #                 ' aloe barbadensis leaf extract': 'aloe barbadensis leaf extract',
    #                 ' aqua (water)': 'water',
    #                 ' water': 'water',
    #                 ' aqua(water)': 'water',
    #                 'aqua': ' water',
    #                 ' water (aqua)': 'water',
    #                 ' water(aqua/eau)': 'water',
    #                 ' water/aqua/eau': 'water',
    #                 ' tremella mushroom extract': 'tremella fuciformis (mushroom) extract',
    #                 'tremella fuciformis extract': 'tremella fuciformis (mushroom) extract',
    #                 ' tremella fuciformis (mushroom) extract': 'tremella fuciformis (mushroom) extract',
    #                 'anona cherimolia fruit extract': 'anthemis nobilis (chamomile) flower oil',
    #                 'aqua (water)': 'water',
    #                 'aqua(water)': 'water',
    #                 'aronia melanocarpa Fruit Extract': 'aronia melanocarpa (black chokeberry) fruit extract',
    #                 'bees wax': 'beeswax',
    #                 'brassica oleracea italica extract': 'brassica oleracea italica (broccoli) extract',
    #                 'camellia sinensis leaf extract': 'camellia sinensis (green tea) leaf extract',
    #                 '*camellia sinensis leaf ext': 'camellia sinensis (green tea) leaf extract',
    #                 'cucumis sativus fruit extract': 'cucumis sativus (cucumber) fruit extract',
    #                 'curcuma longa turmeric root extract': 'curcuma longa (turmeric) root extract',
    #                 'euterpe oleracea fruit extract': 'euterpe oleracea (acai) fruit extract',
    #                 'fragrance(parfum)': 'fragrance (parfum)',
    #                 'fragrance': 'fragrance (parfum)',
    #                 'fragrance/parfum': 'fragrance (parfum)',
    #                 'ginkgo biloba leaf extract': 'ginkgo biloba (ginkgo) leaf extract',
    #                 'glycyrrhiza glabra root extract': 'glycyrrhiza glabra (licorice) root extract',
    #                 'honey / mel / miel': 'honey',
    #                 'hydrogenated poly(c6-14 olefin)': 'hydrogenated poly (c6-14 olefin)',
    #                 'morus alba fruit extract': 'morus alba (white mulberry) fruit extract',
    #                 'olea europaea fruit oil': 'olea europaea (olive) fruit oil',
    #                 'oryza sativa bran oil': 'oryza sativa (rice) bran oil',
    #                 'pelargonium graveolens flower oil': 'pelargonium graveolens (geranium) flower oil',
    #                 'polygonum cuspidatum root extract': 'polygonum cuspidatum (japanese knotweed) root extract',
    #                 'rosa damascena flower oil': 'rosa damascena (rose) flower oil',
    #                 'rosmarinus officinalis leaf extract': 'rosmarinus officinalis (rosemary) extract',
    #                 'saccharum officinarum (sugar cane) extract': 'saccharum officinarum (sugarcane) extract',
    #                 'sugar cane extract': 'saccharum officinarum (sugarcane) extract',
    #                 'sambucus nigra fruit extract': 'sambucus nigra (elder) fruit extract',
    #                 'schisandra chinensis fruit extract': 'schisandra chinensis (schizandra berry) fruit extract',
    #                 'scutellaria baicalensis root extract': 'scutellaria baicalensis (baikal skullcap) root extract',
    #                 'simmondsia chinensis seed oil': 'simmondsia chinensis (jojoba) seed oil',
    #                 'sunflower seed oil': 'helianthus annuus (sunflower) seed oil',
    #                 'strawberry fruit extract': 'fragaria chiloensis (strawberry) fruit extract',
    #                 'tea tree leaf oil': 'melaleuca alternifolia (tea tree) leaf oil',
    #                 'theobroma cacao(cocoa) extract': 'theobroma cacao (cocoa) extract',
    #                 'tocopherol': 'tocopherol (vitamin e)',
    #                 'vitamin e': 'tocopherol (vitamin e)',
    #                 ' bifida ferment lysate': 'bifida ferment lysate',
    #                 ' cetyl ethylhexanoate': 'cetyl ethylhexanoate',
    #                 ' houttuynia cordata extract': 'houttuynia cordata extract',
    #                 ' panax ginseng root extract': 'panax ginseng root extract',
    #                 ' propolis extract': 'propolis extract',
    #                 ' snail secretion filtrate': 'snail secretion filtrate',
    #                 '[hyaluronic acid]': 'hyaluronic acid',
    #                 }

    # def remove_duplicates_set(ingredients_set, replace_dict):

    #     temp = []
    #     for item in ingredients_set:
    #         if item in replace_dict.keys():
    #             temp.append(replace_dict[item])
    #             # print(item)
        
    #     # print("length before: ", len(ingredients_set))
    #     # print("temp length: ", len(temp))

    #     ingredients_set.update(temp)
    #     ingredients_set = ingredients_set - set(replace_dict.keys())
    #     # print("length after: ", len(ingredients_set))
    #     return ingredients_set
    
    # all_bad_ingredients_set = remove_duplicates_set(all_bad_ingredients_set, replace_dict)
    # all_good_ingredients_set = remove_duplicates_set(all_good_ingredients_set, replace_dict)
    # all_ingredients_set = remove_duplicates_set(all_ingredients_set, replace_dict)

    # neutral_ingredients_set = all_bad_ingredients_set & all_good_ingredients_set # intersection

    # print("Updated all bad ingredients number: ", len(all_bad_ingredients_set))
    # print("Updated all good ingredients number: ", len(all_good_ingredients_set))
    # print("Updated all ingredients number: ", len(all_ingredients_set))

    return issues
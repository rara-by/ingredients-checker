import requests
from bs4 import BeautifulSoup
import re

def fetch_webpage(search_term):

    # website search page URL
    url="https://incidecoder.com/"
    url_search = url+"search" 

    # "Benton serum" needs to look like- 'search?query=Benton+serum'
    search_term = search_term.replace(" ", "+")  
    query = {'query': search_term} 

    response = requests.get(url_search, params=query) # GET request

    if response: #check if request was successful
        print("Initial request successful for search page.")   
    else:
        raise Exception(f"Non-success status code: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser") # parse the html document
    search_results = soup.find('div', class_="paddingbl") # target class for search results in this website
    # print(search_results)
    if search_results:
        search_result = search_results.find_next('a', class_="klavika simpletextlistitem") # select the first search result

    # find the relevant url portion
    match = re.search(r'href="(.*?)"', str(search_result))
    if match:
        url_ext = match.group(1)
        # print(url_ext)

    else:
        print("No match found :(")
        return None

    return url + url_ext




def fetch_data(search_term):

    url = fetch_webpage(search_term)

    if not url: #check if previous GET request was successful
        return
    
    response = requests.get(url)

    if response: #check if request was successful
        print("Second request successful for product page.")
        # print(response.text)
    else:
        raise Exception(f"Non-success status code: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser") # parse the html document

    search_results = soup.find_all('meta') # target class for search results in this website
    search_result = search_results[2]["content"].split("explained:") # collect the ingredients list
    ingredients = search_result[1].split(', ')
    product_name = [search_result[0].rsplit(" ", 2)[0]] # collect the product name
    print("Product name: ", product_name[0])

    ingredients = [str.lower(item) for item in ingredients]
    return product_name + ingredients
    
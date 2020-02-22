#get_products.py
#Structure of data is a dictionary/json.

import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"

print("URL:", request_url)

response = requests.get(request_url)
#print(type(response)) #><class 'requests.models.Response'>
#print(dir(response)) #> ['__attrs__', '__bool__', '__class__', ...]

#print(response.status_code) #>200
#print(response.text) #> display each item in the dictionary
#print(type(response.text)) #><class 'str'>

parsed_response = json.loads(response.text)
#print(type(parsed_response))    #><class 'list'>

#To parse a diciontary-like json data, use for loop
for any_item in parsed_response:
    print(any_item["id"], any_item["name"])

first_prod = parsed_response[0]
print("The first product name is ", first_prod["name"])

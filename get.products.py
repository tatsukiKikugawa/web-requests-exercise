#get_products.py
#Structure of data is a dictionary/json.

import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"

print("URL: ", request_url)

response = requests.get(request_url)
print(type(response))
print(dir(response))

print(response.status_code)
print(response.text)
print(type(response.text))

parsed_response = json.loads(response.text)
print(type(parsed_response))    #> list

for any_item in parsed_response:
    print(any_item["id"], any_item["name"])

first_prod = parsed_response[0]
print(first_prod["name"])

#breakpoint()
#type exit in terminal

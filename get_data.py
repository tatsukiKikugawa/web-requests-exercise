#get_data.py
#Structure of data in this url is more like a list than a dictionary

import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"

print("URL: ", request_url)

response = requests.get(request_url)
#print(type(response)) #><class 'dict'>
#print(dir(response))

#print(response.status_code) #>200
print(response.text)
#print(type(response.text)) #><class 'str'>

parsed_response = json.loads(response.text)
#print(type(parsed_response)) #><class 'dict'>
#print(parsed_response["name"])


#breakpoint()
#type exit in terminal


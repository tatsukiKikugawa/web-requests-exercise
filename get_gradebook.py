#get_gradebook.py
#Structure of data is basically a dicrinoary but in the last item
#it has a list of dictoinaries. 

import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"

print("URL: ", request_url)

response = requests.get(request_url)
print(type(response))
#print(dir(response))
print(response.status_code)
#print(response.text)
print(type(response.text))  #>dicrinary?

parsed_response = json.loads(response.text)
print(type(parsed_response))    #>list

breakpoint()

#google keys on dictionaries
#print(parsed_response)
#dir(parsed_response)
#parsed_response.keys()
#parsed_response.values()
#parsed_response.items()
#parsed_response["students"][0]
#grades = [student["finalGrade"] for student in parsed_response["students"]]
#import statistics 
#statistics.mean(grades)

import json
import requests
import statistics

request_url = "https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.json"
response = requests.get(request_url)
parsed_response = json.loads(response.text)

grades = [student["finalGrade"] for student in parsed_response["students"]]

print(grades)
print("Student get the following scores: " + str(grades))

avg_grade = statistics.mean(grades)
print("THE AVERAGE GRADE IS: " + str(avg_grade))


#l = [90, 80, 70]
#print(statistics.mean(l)) #>80

#Use a list comprehension instead of this long line
# grades = []
#for student in parsed_response["students"]:
#    #print(type(student), student)
#    grades.append(student["finalGrade"])
#
#breakpoint()



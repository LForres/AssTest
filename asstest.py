# Automated testing for Assurity Consulting
# Luke Forrester
# 27/09/2022

# Import and load data
import json

f = open('Details.json')
data =  json.load(f)

def test_data(data):                
    # Tests data against defined criteria, returns 1 if data does not meet criteria
    flag=0
    # test if name = badges
    if (data["Name"] != "Badges")|(data["CanRelist"] != True):
        flag=1
        return flag

    # Test if promotion named "feature" contains key phrase
    for prom in data["Promotions"]:
        if prom["Name"] == "Feature":
            if not "Better position in category" in prom["Description"]:
                flag=1
                return flag
    return flag


print(test_data(data))

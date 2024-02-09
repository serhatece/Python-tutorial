import json

person_string = '{"name":"Serhat", "languages":["python","c#"]}'
person_dict = {
    "name": "Ali",
    "languages": ["Python","C#"]
}

# JSON string to Dict

# result = json.loads(person_string)
# result = result["name"] # Serhat
# result = result["languages"] # ["python","c#"]
# result = result["languages"][0] # "python"

# print(type(result)) # class => Dict
# print(result)



# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])


# Dict to JSON string
# result = json.dumps(person_dict)
# print(type(result))


with open("person.json","w") as f:
    json.dump(person_dict,f)

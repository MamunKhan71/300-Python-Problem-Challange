# Problem 124
# Write a Python Program to Create a Nested Dictionary and Access Value
from pprint import pprint

nstDict = {
    "UserName": {
        "Name": "Mamun",
        "Age": "20",
        "Address": "Canada",
    },
    "UserContact": {
        "Phone": "01643091606",
        "Fax": "018895",
    },
}

pprint(nstDict["UserName"]["Address"])
dict = {
    "hello": "hi",
    "name": "madhu",
    "Erp": "200303124142",
    "location": "Vadodara",
    "hobby": ["Reading", "Coading"],
    "bye": "thankyou:)"
}
print(dict["hello"])
print(dict["name"])
print(dict["Erp"])
print(dict["location"])
print(dict["hobby"])
print(dict["bye"])
dict["Erp"] = "200303124143"  # update item mentioned.
del dict["Erp"]               # delete item mentioned.
print(dict)
for i in dict:                # key values will be included in the i.
    print(i)
print(dict.keys())            # input of a dictionary.
print(list(dict))
print(dict.values())          # output of dictionary.
print(dict.items())           # output will be in a list format.
print(str(dict))
string = str(dict)
for i in string:              # make every element and symbol to a invidual string.
    print(i)
print(dict.get("name"))       # get the element mentioned.
print(len(dict))              # length of the dictionary.
list = ["a", "b", "c", "d", "e"]
print(dict.fromkeys(list, 5))
list1 = [1, 2, 3, 4, 5]
# zip fuction to combine lists and out put will be in the form of dictionary.
print({i: j for i, j in zip(list, list1)})
print({i: j+1 for i, j in zip(list, list1)})  # add one to the j of dictionay.
# celsius to fahrenheit conversion.
print({i: (9/5)*j+32 for i, j in zip(list, list1)})

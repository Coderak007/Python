                                  # Dictionary in Python
"""
Dictionaries are used to store data values in key:value pairs ...
They are unordered , mutable & don't allow duplicate keys  

"""
"""

info = { 
    "key" : "value",
    "name" : "aman",
    "age" : 21,
    "marks" : 99.9,
    "fav series " : ("money heist" , "alice in borderland"),
      12 : 89.9
    
}

print(type (info))
print(info["name"])
print(info["marks"])

# ASSIGNING NEW VALUES TO KEY ---

info["name"] = "Aman ojha"
info["surname"] = "ojha"
print(info)

"""

"""

# null dictionary ---
null_dict = {}
null_dict["name"] = "Aman"
print(null_dict)

"""
# nested dictionary ---

"""

student = {
    "name" : "Aman ojha",
    "subjects" : {
        "physics" : 99,
        "chemistry" : 99,
        "maths" : 100,
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["maths"])

"""
# Dictionary methods ---

"""
myDict.keys( ) # returns all keys
myDict.values( ) # returns all values
myDict.items( ) # returns all (key,val) pairs as tuples
myDict.get("key") # returns the key according to the value 
myDict.update(newDict) # inserts the specified items to the dictionary 

"""

                                           # Set in Python

"""
Set is the collection of the unordered items , each element in the set must be unique & immutable.
nums = { 1,2,3,4}
set2 - {1,2,2,2}
# repeated elements stored only once , so it resolved to {1,2}

"""

"""
collection = {1,2,3,4,5 , "mr ak" , "batman"} 

print(collection)
print(type(collection))
print(len(collection))

collection = () # empty set ; syntax

"""
# Set methods ---

"""
set.add(el) # adds an element
set.remove(el) # remove the element
set.clear() # empties the set
set.pop() # removes a random value
set.union(set2) # combines both set values & returns new
set.intersection(set2) # combines commn values & returns new

"""
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))
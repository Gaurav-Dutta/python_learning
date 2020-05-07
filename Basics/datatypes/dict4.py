mydict = dict(
    first_name = "Gaurav",
    last_name = "Dutta",
    city = "Houston"
)
#the value of a key can be changed
#also, we can add new keys and values
mydict["city"] = "Dallas"
mydict["state"] = "Texas"
mydict["zip_code"] = 77077

print( mydict.keys() ) 

#we can also delte a key

mydict.pop("zip_code")

print( mydict.keys() ) 
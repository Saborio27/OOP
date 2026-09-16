mydictionary = {"name1" : "Justus" ,
                "name2" : "Jim" ,
                "name3" : "Joe"
                }
print(mydictionary)

mydictionary.update ({"name4" : "Jemi"})  #adding
mydictionary.update ({"name5" : "Andres"})
mydictionary.update ({"name6" : "Pablo"})

del mydictionary["name6"] #removing

mydictionary["name4"] = "Pillo"  #replacing
print(mydictionary)

fullname = input("enter your full name")
mydictionary.update({"name6" : fullname})
print(mydictionary)





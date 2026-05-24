#my practice code
LahoreInfo = "Lahore is the capital of Punjab and Islamabad is capital of pakistan"
print(LahoreInfo)
print(type(LahoreInfo))

print(LahoreInfo.lower())
print(LahoreInfo.upper())
print(LahoreInfo.title())
print(LahoreInfo.swapcase())
print(LahoreInfo.capitalize())
print(LahoreInfo.count("capital"))

print(LahoreInfo[0:6:1])
print(LahoreInfo[14:22:1])

print(len(LahoreInfo))

#data types - lists

Booklist = [32134 , "The Alchemist", 45678 , 34.5432 , "William Richards"]
print(Booklist)
print(type(Booklist))
print(Booklist[1:12:2])
print(len(Booklist))

for x in Booklist:
    print(x)

Booklist.append(567878)
print(Booklist)

Booklist.insert(2, "i am inserting a sentence")
print (Booklist)


#find string in a string
fruit = 'apple'
print('f' in fruit)

if('a'in fruit):
    print("Found 'a' in fruit named apple")

#String Comparison 
word = 'Ab'
if word == "banana":
    print("Hey bananas.!!")
#A>a
elif word < "banana":
    print("Your word," + word + " less than banana")

#String Library
greet = "Oh Hi Mark!"
low = greet.lower()
print(low)
print(greet.upper())

#Searchoing a String
#find() function is used

fruit = 'banana'
position = fruit.find('na')
print(position)

#Search & Replace
greet = "Hi Mark"
print(greet)
replace_str = greet.replace('Mark','Katie')
print(replace_str)

#Using white spaces

wlc = "     Hola Senorita     "
result = wlc.strip()
print(result)
result2 = wlc.lstrip()
print(result2)

#Check if a string starts with a specific prefix
line = "Next Station Dombivali"
print(line.startswith("Next"))

#Parsing & Extraction
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

#Find posiotion of "@"
atpos = data.find("@")
print(atpos)

#find the next space

spacepos = data.find(" ",atpos) #Start searching from "atpos" variable
print(spacepos)

mailhost = data[atpos+1 : spacepos]
print(mailhost)


#Exercise 6.2 form Dr. Chucks Python Data Structures on Coursera.
#This algorithm will extract the number given in text & print the result.
text = "X-DSPAM-Confidence:    0.8475"

#METHOD-1: 
#finding positions of the respective values.
numStart = text.find("0") 
numEnd = text.find("5")

print(numStart) #print the psotion of 0 i.e. float number start.
print(numEnd) #print the position of 5 i.e. float number end.

#Slice the result from float number starting to the number end.
result = text[numStart : 29]

#print the result converted to a floating point value.
print(float(result)) 

#METHOD-2 :

colPos = text.find(":")
print(colPos)
dataExtract = text[colPos+5:] #slice from beginniong of string upto colon + 4 whitespace i.e. ":" + 4 white spaces.
print(float(dataExtract))

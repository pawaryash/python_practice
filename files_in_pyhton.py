#Lesson 7.1 form Dr. Chucks Python Data Structures on Coursera.
#newline character "\n"
stuff = "Hello\nWorld"
print(stuff)
print(len(stuff))

#Spoecify the path pf the file to be opened for manipulation using "open()". 
fhand = open("C:/Users/yashp/Documents/CODE/Python/files_manipulation/mbox.txt")
counter = 0
for lines in fhand:
    counter += 1
print('Line Count: ', counter)

#Reading the whole file (including new lines) in a single string using ".read()".
fhand = open("C:/Users/yashp/Documents/CODE/Python/files_manipulation/mbox.txt")
inp = fhand.read()
print(len(inp))
print(inp[:20]) #read from start upto 20th character

string = "From stephen.marquar"
count=0
for char in string:
    count += 1
print(count)


#Search through the file using if statements to add some conditions in the search criteria.
fhand = open("C:/Users/yashp/Documents/CODE/Python/files_manipulation/mbox.txt")
for line in fhand:
    if line.startswith("From: "):
        #Truncating "From: "
        mailPos = line.find(":")
        mailExtract = line[mailPos+2:]
        #The lines in the text file already has lines seperated by new lines.
        #The print statement also automatically seperated two lines with a new line.
        #so we are seeing two new lines in the output.
        #To rectify this we'll use ".rstrip()" to remove reove white spavces from right side.
                 
        mailExtract = mailExtract.rstrip()
        print(mailExtract)

#Skipping with continue.
#We can skip a line by using a continue statement
fhand = open("C:/Users/yashp/Documents/CODE/Python/files_manipulation/mbox.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From: "):
        continue #continue goes back to the top of the loop, skip the unwanted line & check the next line.
    print(line)


#Using "in" to select lines
# We can look for a string anywhere in an line as our selection criteria

fhand = open("C:/Users/yashp/Documents/CODE/Python/files_manipulation/mbox.txt")
for line in fhand:
    line = line.rstrip()
    if not "@uct.ac.za" in line:
        continue
    print(line)

#Prompt for a file name 
fname = input("Enter the file name: ") #Enter file name with extension
try: 
    fhand = open(fname)
except:
    print('File not found or incorrect file name:',fname)
    quit() #this statemnt will terminate the program execution.
count = 0
for lines in fhand:
    if lines.startswith("Subject: ") :
        count+=1
print("There are", count, "subject lines in file: ",fname)
#7.1 Write a program that prompts for a file name, 
#then opens that file and reads through the file, and print the contents of the file in upper case. 


filename = input("Enter file name: ")
#give a handle to the file. So it can be operated upon.
file = open(filename)
filestr = file.read()
print(filestr.upper().rstrip()) #strip extra lines

print("-----------------------------------------------------------------")
#OR
file2 = open("words.txt")
for lines in file2:
    
    print(lines.upper().rstrip())
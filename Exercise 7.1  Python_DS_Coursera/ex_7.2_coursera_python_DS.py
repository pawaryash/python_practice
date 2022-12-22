#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#ou can download the sample data at http://www.py4e.com/code3/mbox-short.txt


filename = input("Enter file name: ")
file = open(filename)

count = 0
for lines in file:
    if not lines.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    extract = lines.find(":")
    data = lines[extract+2:]
    #data = float(data)
    #print(data)
    data = data.split()
    print(data)



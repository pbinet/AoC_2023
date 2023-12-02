import os

input_file = "01_Input.txt"
#input_file = "01_Example.txt"

answer = 0
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

f = open(input_file,"r")
for line in f:
    a = ""
    b = ""
    i = 0
    while a == "":
        if line[i:i+1] in numbers: a = line[i:i+1]
        i += 1

    i = len(line) -1
    while b == "":
        if line[i:i+1] in numbers: b = line[i:i+1]
        i -= 1
    a = a + b 
       
    answer += int(a)


print (answer)
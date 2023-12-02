import os

input_file = "01_Input.txt"
#input_file = "01_Example.txt"
#input_file = "01_Example_2.txt"
answer = 0
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lettered_numbers = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

f = open(input_file,"r")
for line in f:
    a = ""
    b = ""
    i = 0
    #print("\n" + line)
    while a == "":
        if line[i:i+1] in numbers: a = line[i:i+1]
        for num in lettered_numbers.keys():
            if line[i:i+len(num)] == num : a = lettered_numbers[num]
            #print(num + "  " + line[i:i+len(num)] + "     a:" + a)
        i += 1

    i = len(line) -1
    while b == "" and i > 0:
        if line[i-1:i] in numbers: b = line[i-1:i]
        for num in lettered_numbers.keys():
            if line[i-len(num):i] == num : b = lettered_numbers[num]
            #print(num + "  " + line[i-len(num):i] + "     b:" + b)
        i -= 1
    print( line[:-1] + " --> " +a + " - " + b)
    a = a + b
  
       
    answer += int(a)


print (answer)
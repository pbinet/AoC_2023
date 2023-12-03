import os

input_file = "03_Input.txt"
#input_file = "03_Example.txt"
#input_file = "01_Example_2.txt"


def is_special_chars(a):
    if not a.isdigit() and not a.isalpha() and a != "." : 
         return True
    else:
        return False


answer1 = 0
answer2 = 0


f = open(input_file,"r", encoding="utf-8")
inputs = f.read().splitlines()
toto = [input for input in inputs]
len_line = len(toto[0])

for line_num in range(len(toto)):
    line = toto[line_num][:-1]
    c = 0
    while c < len_line:
        # print(c)
        # print(line[c:c+1])
        if line[c:c+1].isdigit():
            i = 1
            while line[c+i:c+i+1].isdigit(): i +=1
            part_num = int(line[c:c+i])
            ok = "-"


            if c-1 > 0: 
                if is_special_chars(line[c-1:c]): 
                    ok = part_num
                    print("line " + str(line_num + 1) + ": " + str(part_num) + " found left")
            if i < len_line: 
                if is_special_chars(line[c+i:c+i+1]):
                    ok = part_num
                    print("line " + str(line_num + 1) + ": " + str(part_num) + " found right")
            if line_num > 0:
                for a in range(max(0,c-1), min(len_line, c + i + 1)):
                    if is_special_chars(toto[line_num-1][a:a+1]): 
                        ok = part_num
                        print("line " + str(line_num + 1) + ": " + str(part_num) + " found above " + toto[line_num-1][a:a+1])
            if line_num < len(toto)-1:
                for a in range(max(0,c-1), min(len_line, c + i + 1)):
                    if is_special_chars(toto[line_num+1][a:a+1]) : 
                        ok = part_num
                        print("line " + str(line_num + 1) + ": " + str(part_num) + " found below " + toto[line_num+1][a:a+1] + " " + str(c) + " " + str(i) + " " + str(a) )

            #print(str(part_num) + "  " + str(ok))
            if str(ok) != "-" : answer1 += ok
            

            c += i
        c += 1 


print(answer1)
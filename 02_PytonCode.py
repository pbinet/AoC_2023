import os

input_file = "02_Input.txt"
#input_file = "02_Example.txt"
#input_file = "01_Example_2.txt"


answer1 = 0
answer2 = 0
input_colors =  { "red":12, "green":13, "blue":14}

f = open(input_file,"r")
for line in f:
    game = { "red": 0, "green": 0, "blue": 0}
    data = line.split(":")
    #print(data[0][5:])
    game_num = int(data[0][5:])
    data[1] = data[1].replace("; ",",")
    data[1] = data[1].replace(", ",",")
    print(data[1][1:-1])
    data = data[1][1:-1].split(",")
    for input in data:
        detail = input.split(" ")
        #print(input + "   ---->    " + detail[1] + "-" + detail[0] + "-")
        game[detail[1]] = max(int(detail[0]) , game[detail[1]] )

    print(game)
    ok = True
    power = 1
    for color in input_colors:
        if game[color] > input_colors[color]: 
            ok = False
            print(color + " " + str(game[color]) + " > " + str(input_colors[color]))
        power = power * game[color]
    if ok: 
        print ("Game " + str(game_num) + " ok |   " + str(answer1) + " + " + str(game_num) )
        answer1 += game_num
    else: print ("Game " + str(game_num) + " ko")
    answer2 += power
    print("power = " + str(power) + "  -->  " + str(answer2) + "\n")

print("Answer 1: " + str(answer1))
print("Answer 2: " + str(answer2))
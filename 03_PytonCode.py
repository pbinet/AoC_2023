import os

input_file = "03_Input.txt"
input_file = "03_Example.txt"




inputs_1 = ['.......#40..........*.....#...@....473.......789................/...*.......902......987..........179......*.................382..519.......',
            '......................*.......11...............................926..153.#.................725*................................*.....*.......',
            '...358...527..345..746.978....................*.........................607..798..899.........86.........*478.......888....949..767..807....',
            '.....*...*.......%..............743*715..723...56................81.........*....=........345.........802.......776*...............$........']

inputs_2 = ['......................881...........*............................989......+....235..............491...*...-.....693.........16..............',
            '........957......614..553....345*56......#..................*...658.870........895......%........714......749...13..........................',
            '...........$....................................127........775.....*......988..*.........254.276.................*..560.950.............*...',
            '....761.................................825.........495..............496.....+.87.............*....*....689..26....*.....*...........131.745']

inputs_3 = ['467..114..',
            '...*......',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..']

inputs_4 = ['.....#....*.....................779..........*......140.24....................22.........@..28..............................................',
            '.......682.....348+.153.168@......%.451.627.236.............92.141.....393........669.....................75.......557...585...826......559.',
            '......................*.............*............881.........*....*776...*.105......*...=....#....&........&.526..+............#........%...',
            '....95.....410......566..760....760........586....*....*...560........548.......335...951...749...256.........*......313....$...888........']





def is_special_chars(a):
    if not a.isdigit() and not a.isalpha() and a != "."  and a != "\n" and a != "" : 
         return True
    else:
        return False


def get_gears_value(line_num, c):
    a = 0
    b = 0
    while toto[line_num][c].isdigit() and a > -1:
        print("a " + str(a))
        a -= 1 
    while toto[line_num][c].isdigit() and  b < len_line:
        print("b")
        b += 1

    print("get_gears_value" + toto[line_num][a + 1:b-1])
    return toto[line_num][a + 1:b-1]


answer1 = 0
answer2 = 0
numbers_to_keep = []

f = open(input_file,"r", encoding="utf-8")
inputs = f.read().splitlines()
f.close()
toto = [input for input in inputs]
print(toto)

#toto = inputs_4


len_line = len(toto[0])

for line_num in range(len(toto)):
    line = toto[line_num]#[:-1]
    c = 0
    while c < len_line:
        # print(c)
        # print(line[c:c+1])
        if line[c:c+1].isdigit():
            i = 1
            while line[c+i:c+i+1].isdigit(): i +=1
            part_num = int(line[c:c+i])
            #
            # print(part_num)
            ok = "-"

            if part_num == 717: print("*************************************************************************************")

            if c-1 > 0: 
                if is_special_chars(line[c-1:c]): 
                    ok = part_num
                    print("line " + str(line_num + 1) + ": " + str(part_num) + " found left " + line[c-1:c])
            if i < len_line: 
                if is_special_chars(line[c+i:c+i+1]):
                    ok = part_num
                    print("line " + str(line_num + 1) + ": " + str(part_num) + " found right " + line[c+i:c+i+1])
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
            if str(ok) != "-" : 
                answer1 += ok
                numbers_to_keep.append(ok)
            

            c += i
        c += 1 

#print(numbers_to_keep)
#print(len(numbers_to_keep))
print("Answer1 = " + str(answer1) + "\n\n")
#  536688 not ok



# Looking at all gears
gears_locations = []

for line_num in range(len(toto)):
    c = 0
    for c in range(len_line):
        if toto[line_num][c:c+1] == "*" : gears_locations.append([line_num,c])
        

print (gears_locations)
print (len(gears_locations))

gears_details = []

# find gears values
for gear in gears_locations:
    print(gear)

    gear_details = []
    #row above

    num_line = gear[0]
    c = gear[1]

    if num_line > 0:
        if toto[num_line-1][c:c+1].isdigit(): 
            gears_details.append(get_gears_value(num_line-1,c))
        else:
            if toto[num_line-1][c-1:c].isdigit() and not toto[num_line-1][c+1:c+2].isdigit(): gears_details.append(get_gears_value(num_line-1,c-1))
            if not toto[num_line-1][c-1:c].isdigit() and toto[num_line-1][c+1:c+2].isdigit(): gears_details.append(get_gears_value(num_line-1,c+1))
            if  toto[num_line-1][c-1:c].isdigit() and toto[num_line-1][c+1:c+2].isdigit(): 
                gears_details.append(get_gears_value(num_line-1,c-1))
                gears_details.append(get_gears_value(num_line-1,c+1))

    if num_line < len(toto):
        if toto[num_line+1][c:c+1].isdigit(): gears_details.append(get_gears_value(num_line+1,c))
        else:
            if toto[num_line+1][c-1:c].isdigit() and not toto[num_line+1][c+1:c+2].isdigit(): gears_details.append(get_gears_value(num_line+1,c-1))
            if not toto[num_line+1][c-1:c].isdigit() and toto[num_line+1][c+1:c+2].isdigit(): gears_details.append(get_gears_value(num_line+1,c+1))
            if  toto[num_line+1][c-1:c].isdigit() and toto[num_line-1][c+1:c+2].isdigit(): 
                gears_details.append(get_gears_value(num_line+1,c-1))
                gears_details.append(get_gears_value(num_line+1,c+1))

    if c > 0 :
        if toto[num_line][c-1:c].isdigit(): gears_details.append(get_gears_value(num_line,c-1))

    if c < len_line :
        if toto[num_line][c+1:c+2].isdigit(): gears_details.append(get_gears_value(num_line,c+1))


    print(gear_details)




import os
import re


input_file = "08_Input.txt"
#input_file = "08_Example_1.txt"
#input_file = "08_Example_2.txt"
#input_file = "08_Example_3.txt"

answer1 = 0
map = {}

f = open(input_file,"r", encoding="utf-8")
inputs = f.read().splitlines()
f.close()

instructions = [*inputs[0]]
print(instructions)

nodes = [input for input in inputs]
print(nodes)
for i in range(len(nodes)):
    if i > 1: 
        map[nodes[i][:3]] =  [nodes[i][7:10], nodes[i][12:15]]
    i += 1

print(map)

i = 0
current_node = 'AAA'
while current_node != "ZZZ" :
    if instructions[i % len(instructions)] == "L": 
        current_node = map[current_node][0]
    else:
        current_node = map[current_node][1]
    i += 1

print (i)
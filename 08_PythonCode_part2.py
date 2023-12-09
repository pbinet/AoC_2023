import os
import re
import time


input_file = "08_Input.txt"
#input_file = "08_Example_1.txt"
#input_file = "08_Example_2.txt"
#input_file = "08_Example_3.txt"



def is_Z(current_nodes):
    a = True
    for node in current_nodes.keys():
        #print(current_nodes[node][2:3])
        if current_nodes[node][2:3] != "Z": a = False
    return(a)



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


answer2 = 0
current_nodes = {}
for node in map.keys():
    if node[2:3] == "A":
        current_nodes[node] = node
        

print(len(current_nodes))

i = 0
while not is_Z(current_nodes) :
    if instructions[i % len(instructions)] == "L": j = 0
    else: j = 1
    for node in current_nodes.keys():
        current_nodes[node] = map[current_nodes[node]][j]
    i += 1
    #print(current_nodes)
    #time.sleep(1)
    
    if i % 1000 == 0 : print(i)


print (i)
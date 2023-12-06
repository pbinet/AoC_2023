import os
import re
import math 

input_file = "06_Input.txt"
#input_file = "06_Example.txt"



answer1 = 1
answer2 = 0
numbers_to_keep = []

seeds_detail ={}
cards_win ={}
cards_distrib = {}

f = open(input_file,"r", encoding="utf-8")
inputs = f.read().splitlines()
f.close()
lines = [input for input in inputs]
times = lines[0].split(":")
times = times[1].replace(" ","")
times = re.findall(r"\d+", times)
distances = lines[1].split(":")
distances = distances[1].replace(" ","")
distances = re.findall(r"\d+", distances)

for i in range(len(distances)):
    dist = int(distances[i])
    time = int(times[i])
    print("Time " + str(time) + " | dist " + str(dist))
    winning_try = 0
    t = 0
    for t in range(time):
        t += 1
        projected =  t * (time-t)
        # print(str(t) + " : projected " + str(projected) + " / " + str(dist))
        if projected > dist : winning_try +=1
    print (winning_try)
    answer1 = answer1 * winning_try


    

print("\n\nAnswer 1 = " + str(answer1) + "\n\n")
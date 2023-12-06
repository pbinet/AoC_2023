import os
import re

input_file = "05_Input.txt"
#input_file = "05_Example.txt"



answer1 = 0
answer2 = 0
numbers_to_keep = []

seeds_detail ={}
cards_win ={}
cards_distrib = {}

f = open(input_file,"r", encoding="utf-8")
inputs = f.read().splitlines()
f.close()
lines = [input for input in inputs]


seeds = re.findall(r"\d+", lines[0])
print(seeds)
for seed in seeds: seeds_detail[seed] = [int(seed)]
print(seeds_detail)
i = 1
target_column = 0
while i < len(lines):
    if lines[i].find("map:") > 0: 
        target_column += 1
        for key in seeds_detail.keys():
            seeds_detail[key].append(seeds_detail[key][target_column-1])
        print(seeds_detail)

    if len(lines[i]) == 0:
        print(seeds_detail)
        print("Toto !")

    if lines[i][:1].isdigit():
        data = re.findall(r"\d+",lines[i])
        destination_range_start = int(data[0])
        source_range_start = int(data[1])
        range_length = int(data[2])
        diff = destination_range_start - source_range_start

        for key in seeds_detail.keys():
            if seeds_detail[key][target_column-1] >= source_range_start and seeds_detail[key][target_column-1] < (source_range_start + range_length) : 
                seeds_detail[key][target_column] = seeds_detail[key][target_column] + diff

    i += 1
    

print(seeds_detail)

min_loc = seeds_detail[seeds[1]][target_column]
for key in seeds_detail.keys():
    if seeds_detail[key][target_column] < min_loc : 
        min_loc = seeds_detail[key][target_column]
        answer1 = key

print("\n\nAnswer 1 = " + str(min_loc) + "\n\n")
print("\n\nAnswer 2 = " + str(answer2) + "\n\n")



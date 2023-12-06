import os
import re

input_file = "04_Input.txt"
#input_file = "04_Example.txt"




answer1 = 0
answer2 = 0
numbers_to_keep = []

cards_detail ={}

f = open(input_file,"r", encoding="utf-8")
inputs = f.read().splitlines()
f.close()
cards = [input.split(":") for input in inputs]
print(cards)
for card in cards:
    cards_detail[card[0]] = card[1].split("|")
    winning_nums = re.findall(r"(\d+)", card[1].split('|')[0])
    picked_nums = re.findall(r"(\d+)", card[1].split('|')[1])
    #winning_nums= winning_nums.split[" "]
    print(winning_nums)
    print(picked_nums)

    nb_points = 0
    for i in picked_nums:
        if i in winning_nums:
            if nb_points == 0: nb_points = 1
            else : nb_points = nb_points * 2

    print("Points for " + str(card[0])+ " = " + str(nb_points) + "\n")
    answer1 += nb_points


print("\n\nAnswer 1 = " + str(answer1))
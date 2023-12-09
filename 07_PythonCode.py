import os
import re
import math 

input_file = "07_Input.txt"
#input_file = "07_Example.txt"


answer1 = 0

cards_values = {"A":32, "K":27, "Q":12, "J":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
ranks = []

f = open(input_file,"r", encoding="utf-8")
inputs = f.read().splitlines()
f.close()
cards = [input[:5] for input in inputs]
bets = [int(input[6:]) for input in inputs]
print(cards)
print(bets)

for card in cards:
    rank = 0
    value = 0
    for a in cards_values:
        if card.count(a) == rank // 10 and rank == 20 :
            rank = 25
        if card.count(a) == 3 and rank == 20 :
            rank = 32
        if card.count(a) == 2 and rank == 30 :
            rank = 32
        if card.count(a) > rank // 10 : 
            rank = card.count(a) * 10

    for i in range (len(card)):
        value += cards_values[card[i:i+1]] * 100 ** (5-i-1)
        #print(value)

    totalrank = rank * 100 ** 6 + value
    ranks.append(totalrank)
    print(card + " rank: " + str(rank)+ " value: " + str(value) + " totalrank: " + str(totalrank) + "\n")


sorted_ranks = ranks.copy()
sorted_ranks.sort()


print(ranks)
print(sorted_ranks)


rank = 0
for i in range(len(sorted_ranks)):
    if sorted_ranks[i] == rank : "\n\n   ****************\n   DUPLICATE " + str(rank)
    rank = sorted_ranks[i]
    for j in range(len(sorted_ranks)):
        if ranks[j] == sorted_ranks[i] : 
            answer1 += bets[j] * (i +1)
            print(" > " + cards[j] + "  bet " + str(bets[j]) + "  multiplier " + str(i +1)  + "        " + str(answer1) )


print("\n\nAnswer 1 = " + str(answer1) + "\n\n")

# Answer from Hugo   241344943
print(str(241344943/answer1))
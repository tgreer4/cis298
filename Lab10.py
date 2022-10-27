#Lab 10 & Takehome TGreer
from audioop import reverse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def position_count(letter, dict):
    if(letter in dict): dict[letter] += 1
    else: dict[letter] = 1

alphabet, pos0, pos1, pos2, pos3, pos4= {}, {}, {}, {}, {}, {}

with open("answers.txt", 'r') as f: #open file
    with open("letter_count.txt",'w') as wow:
        for line in f:
            split_lines = line.split(" ")
            for word in split_lines:
                for b in range(len(word)): #iterates through word to look for occurrences of a letter
                    char = word[b].upper()
                    if(char == "\n"): continue 
                    else: position_count(char, alphabet)

                    if(b ==0) : position_count(char, pos0)
                    elif(b ==1) : position_count(char, pos1)
                    elif(b ==2) : position_count(char, pos2)
                    elif(b ==3) : position_count(char, pos3)
                    else: position_count(char, pos4)

        sorted_alph = dict(sorted(alphabet.items()))
        sorted_pos0 = dict(sorted(pos0.items(), key=lambda x: x[1], reverse=True))
        sorted_pos1 = dict(sorted(pos1.items(), key=lambda x: x[1], reverse=True))
        sorted_pos2 = dict(sorted(pos2.items(), key=lambda x: x[1], reverse=True))
        sorted_pos3 = dict(sorted(pos3.items(), key=lambda x: x[1], reverse=True))
        sorted_pos4 = dict(sorted(pos4.items(), key=lambda x: x[1], reverse=True))
        wow.write("Sorted Alpha: {}".format(str(sorted_alph)))
        wow.write("\n\nSorted Pos0: {}".format(str(sorted_pos0)))
        wow.write("\n\nSorted Pos1: {}".format(str(sorted_pos1)))
        wow.write("\n\nSorted Pos2: {}".format(str(sorted_pos2)))
        wow.write("\n\nSorted Pos3: {}".format(str(sorted_pos3)))
        wow.write("\n\nSorted Pos4: {}".format(str(sorted_pos4)))
'''
max_key = max(sorted_alph, key = sorted_alph.get)
plt.annotate('Highest Count', xy=(max_key, sorted_alph[max_key]))
plt.bar(sorted_alph.keys(), sorted_alph.values(), edgecolor = "white") #correct
plt.title("Count of Alphabetic Characters in answers.txt")
plt.xlabel("Alphabetic Charaacters")
plt.ylabel("Count")
plt.show()

max_key0 = max(sorted_pos0, key = sorted_pos0.get)
plt.annotate('Highest Count', xy=(max_key0, sorted_pos0[max_key0]))
plt.bar(sorted_pos0.keys(), sorted_pos0.values(), edgecolor = "white") #correct
plt.title("Count of Alphabetic Characters in Position 1")
plt.xlabel("Alphabetic Charaacters")
plt.ylabel("Count")
plt.show()

max_key1 = max(sorted_pos1, key = sorted_pos1.get)
plt.annotate('Highest Count', xy=(max_key1, sorted_pos1[max_key1]))
plt.bar(sorted_pos1.keys(), sorted_pos1.values(), edgecolor = "white") #correct
plt.title("Count of Alphabetic Characters in Position 2")
plt.xlabel("Alphabetic Charaacters")
plt.ylabel("Count")
plt.show()

max_key2 = max(sorted_pos2, key = sorted_pos2.get)
plt.annotate('Highest Count', xy=(max_key2, sorted_pos2[max_key]))
plt.bar(sorted_pos2.keys(), sorted_pos2.values(), edgecolor = "white") #correct
plt.title("Count of Alphabetic Characters in Position 3")
plt.xlabel("Alphabetic Charaacters")
plt.ylabel("Count")
plt.show()

max_key3 = max(sorted_pos3, key = sorted_pos3.get)
plt.annotate('Highest Count', xy=(max_key3, sorted_pos3[max_key]))
plt.bar(sorted_pos3.keys(), sorted_pos3.values(), edgecolor = "white") #correct
plt.title("Count of Alphabetic Characters in Position 3")
plt.xlabel("Alphabetic Charaacters")
plt.ylabel("Count")
plt.show()

max_key4 = max(sorted_pos4, key = sorted_pos4.get)
plt.annotate('Highest Count', xy=(max_key4, sorted_pos4[max_key]))
plt.bar(sorted_pos4.keys(), sorted_pos4.values(), edgecolor = "white") #correct
plt.title("Count of Alphabetic Characters in Position 5")
plt.xlabel("Alphabetic Charaacters")
plt.ylabel("Count")
plt.show()
'''
alphabet2 = { #skeleton that will hold dicts pos0-pos1, used a 2level nested dictionary
    'A':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'B':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'C':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'D':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'E':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'F':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'G':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'H':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'I':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'J':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'K':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'L':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'M':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'N':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'O':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'P':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'Q':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'R':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'S':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'T':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'U':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'V':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'W':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'X':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'Y':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
    'Z':{'Position 1': 0, 'Position 2': 0, 'Position 3': 0, 'Position 4': 0, 'Position 5': 0},
}

for a in alphabet2: #filling up 2level dictionary
    alphabet2[a]['Position 1'] = pos0[a]
    alphabet2[a]['Position 2'] = pos1[a]
    alphabet2[a]['Position 3'] = pos2[a]
    alphabet2[a]['Position 4'] = pos3[a]
    alphabet2[a]['Position 5'] = pos4[a]
color = ['#E8A49C','#3C4CAD','#240E88','#F04393', '#F9C449'] #used to color bar graph
pd.DataFrame(alphabet2).T.plot.bar(color = color) #plotting grouped bar graph
#various labels for graph
plt.title("Count of Alphabet throughout Each Position Grouped By Letter")
plt.xlabel("Alphabet")
plt.ylabel("Count")
plt.xticks(rotation = 0) #makes xticks readable by havig rotation set to 0
plt.legend(loc = 1) #location of legend
plt.show()

pd.DataFrame(alphabet2).T.plot.bar(color = color, stacked = True) #how to do a stacked bar graph
plt.title("Count of Alphabet throughout Each Position Grouped By Letter")
plt.xlabel("Alphabet")
plt.xticks(rotation = 0)
plt.legend(loc = 1)
plt.ylabel("Count")
plt.show()

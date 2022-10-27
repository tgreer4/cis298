#TGreer Lab 8
from audioop import reverse
import matplotlib.pyplot as plt
import numpy as np
import string

#q1
letter_num = {}

with open("CIS298.txt", encoding = 'utf-8') as f: #open file
    for char in f.read(): #iterate through file char by char
        if(char.isalpha()): #alpha character
            char = char.lower()
            if(char in letter_num): letter_num[char] += 1
            else: letter_num[char] = 1
        elif (char.isnumeric()): #numbers
            if(str(char) in letter_num): letter_num[str(char)] += 1
            else: letter_num[str(char)] = 1
        else:
            continue
sorted_letter = dict(sorted(letter_num.items())) #change to make code corrrect
#plt.bar(sorted(letter_num.keys()), letter_num.values(), edgecolor = "white") incorrect way
plt.bar(sorted_letter.keys(), sorted_letter.values(), edgecolor = "white") #correct
plt.title("Count of Alphanumeric Characters in CIS298.txt")
plt.xlabel("Alphanumeric Charaacters")
plt.ylabel("Count")
plt.legend()
plt.show()

#q2
punc = ['!', '\"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '/', '_', '`', '{', '|', '}', '~', " ", "\n"]
word_count = {}
punc_num_dict = {}

with open("Frankenstein.txt", encoding = 'utf-8') as f: #open file
    for line in f: #iterate through file via lines
        for word in line.split(" "): #splits line up by spaces
            word = word.lower()
            for char in word: 
                if(char in punc): #check for punctuation
                    if(char == "'" or char =='"' or char == '`' or char.isspace()): word = word.replace(char, "")
                    elif(char in punc_num_dict): punc_num_dict[char] += 1
                    else: punc_num_dict[char] = 1
                    word = word.replace(char, "")

                elif(char.isnumeric()): #check for numbers
                    if(char in punc_num_dict): punc_num_dict[str(char)] += 1
                    else: punc_num_dict[str(char)] = 1
                    word = word.replace(char, "")

            if(word in word_count): word_count[word] += 1 #check for words
            else: word_count[word] = 1
print(word_count)
sorted_word = {k: v for k, v in sorted(list(word_count.items()), key=lambda item: item[1], reverse = True)[:50]}
# plt.bar(sorted_word.keys(), sorted_word .values(), edgecolor = "white")
# plt.xticks(rotation = 90)
# plt.title("Count of Most Used Words in Frankenstein.txt")
# plt.xlabel("Words")
# plt.ylabel("Count")
# plt.show() 

# sorted_wordLen = {k: v for k, v in sorted((word_count.items()), key=lambda item: len(item[0]), reverse = True)[:50]}
# #print(sorted_wordLen.keys(), len(sorted_wordLen.keys()))
# x_axis = list(sorted_wordLen.keys())
# y_axis = list(sorted_wordLen.values())
# plt.barh(x_axis, y_axis)
# plt.title("Count of Longest Words in Frankenstein.txt")
# plt.ylabel("Words")
# plt.xlabel("Count")
# plt.show() 
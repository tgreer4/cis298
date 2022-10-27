#Lab 9 TGreer
import csv
from statistics import mean
import statistics

class disqualifier(Exception):
    def __init__(self, text):
        self.value = text

total_scores, names, raw_round_scores, round_scores, total_scores_without= [], [], [], [], []
temp_score,temp_score2  = 0, 0
with open("scores.csv", 'r') as f: #open file
    with open("output_9.txt", 'w') as b:
        
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            name = row[1] + ' ' + row[0] #takes the name
            names.append(name)

            scores = row[2:] #reads in row as a string
            for a in range(len(scores)): scores[a] = int(scores[a]) #castes it as an int
            
            '''
            raw_round_scores.append(row[2:]) #used later to evaluate mean etc
            for a in range(len(raw_round_scores)): 
                for b in range(len(raw_round_scores[a])): raw_round_scores[a][b]= int(raw_round_scores[a][b])
            '''

            indices = ''#checking for disqualifier
            for a in range(len(scores)): 
                try:
                    if (scores[a] == -1): 
                        indices += str(a+1) + ' '
                        raise disqualifier("{} has been disqualified from round {} ".format(name, a+1))
                    else: temp_score2 += scores[a]
                except disqualifier as err:
                    print(err)
            total_scores_without.append(temp_score2)
            temp_score2 = 0

            if(indices != ''): 
                b.write('{} didn\'t participate in round(s): {}\n'.format(name, indices))
                indices = ' '
            
            for a in range(len(scores)): #adds up scores
                temp_score += int(scores[a])
            total_scores.append(temp_score)
            temp_score = 0

''' coudn't figure out how to read in only rows and account for disqualified players
for a in range(len(raw_round_scores)): 
    for b in range(len(raw_round_scores[a])):
        if (raw_round_scores[a][b] == -1): continue
        else: round_scores[b] += raw_round_scores[a][b]
print(round_scores)
'''

with open("results_9.txt", 'w') as b:
    for a in range(len(names)):
        b.write('Player {} with total score of {}\n'.format(names[a], total_scores[a]))
    high_score = 0
    player = ' '
    for a in range(len(total_scores)): # starts at 1
        if(a == 0):
            high_score = total_scores[a]
            player = names[a]
        elif(high_score < total_scores[a]):
            high_score = total_scores[a]
            player = names[a]
        else:  continue
    b.write('\n\nPlayer with highest score is {} with {}.\n'.format(player, high_score))

    for a in range(len(total_scores)): # starts at 1
        if(a == 0):
            high_score = total_scores[a]
            player = names[a]
        elif(high_score > total_scores[a]):
            high_score = total_scores[a]
            player = names[a]
        else: continue
    b.write('Player with lowest score is {} with {}.\n'.format(player, high_score))
    b.write("Mean of total qualified scores: {:.1f} Median of total qualified scores: {:.1f}".format(statistics.mean(total_scores_without), statistics.median(total_scores_without)))
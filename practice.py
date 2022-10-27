from traceback import print_tb


with open("CIS298.txt", encoding = 'utf-8') as f: #open file
    for line in f: #iterate through file char by char
        print(line, " ")
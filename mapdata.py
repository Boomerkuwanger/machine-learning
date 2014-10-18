import os
import sys
import champions
num_champs = len(champions.champions)

data_file = str(sys.argv[1]) 
training_examples_file = open(str(sys.argv[2]), 'w')
predictions_file = open(str(sys.argv[3]), 'w')
blue_team = [0] * num_champs
red_team = [0] * num_champs
games = []

def print_array(arr):
    string_data = ''
    result = arr.pop()
    print result
    for dat in arr:
        string_data = string_data + str(dat) + ','

    breaker = "----------------------------------"

    if result >= 0:
        f = open(training_examples_file ,'w')
        f.write(string_data + str(result) + '\n')
    else: 
        string_data = string_data.strip(',')
        f = open(predictions_file, 'w')
        f.write(string_data + '\n')
    f.close()

    string_data = string_data.strip(',')
    print breaker
    print string_data

i = 0
for line in open(data_file):
    line = line.strip('\n')

    if i == 0:
        for x in range(num_champs):
            blue_team = [0] * num_champs
            red_team = [0] * num_champs
        result = -1

    i += 1
    if line in champions.champions:
        line_no = champions.champions[line] 
    else:
        line_no = int(line)

    #print line_no

    if not i % 11:
        red_team.append(line_no)
        games.append(blue_team+red_team)
        i = 0
    elif i > 5:
        red_team[line_no - 1] = 1
    else:
        blue_team[line_no - 1] = 1

for i in range(len(games)):
    print_array(games[i])

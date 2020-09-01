#### script ####
voter_id =[]
County = []
Candidate = []
with open('Resources/election_data.csv','r') as poll:
    for counter,line in enumerate(poll):
        if counter!=0:
            line = line.strip("\n").split(",")
            voter_id.append(line[0])
            County.append(line[1])
            Candidate.append(line[2])

################ calculations ##################
#1) store details in dictionary
candidate = {}
for candi in Candidate:
    if candi not in candidate:
        candidate[candi] =1
    else:
        candidate[candi] +=1
        
#2) modified
candidate1 = {k:[candidate[k],round(candidate[k]*100/len(voter_id),0)] for k in candidate}

#3) Winner
win = 0
winner = 0
for key in candidate1:
    if candidate1[key][0]>win:
        win = candidate1[key][0]
        winner = key
        
##### writing to text file ######

with open('analysis/poll.txt','w') as file:
    file.write('Election Results\n')
    file.write("----------------------\n")
    file.write("Total Votes: {}\n".format(len(voter_id)))
    file.write("----------------------\n")
    for key in candidate1:
        file.write("{}: {}00% ({})\n".format(key,candidate1[key][1],candidate1[key][0]))
    file.write("----------------------\n")
    file.write("Winner: {}\n".format(winner))
    file.write("----------------------\n")
    file.close()
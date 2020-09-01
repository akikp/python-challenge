#### script ####
timeframe =[]
profit_loss = []
with open('Resources/budget_data.csv','r') as budget:
    for counter,line in enumerate(budget):
        if counter!=0:
            line = line.strip("\n").split(",")
            timeframe.append(line[0])
            profit_loss.append(int(line[1]))

################ calculations ##################
# 1)
change = 0
for i in range(0,len(profit_loss)-1):
    diff = profit_loss[i+1] - profit_loss[i]
    change += diff
avg_change = change/(len(profit_loss)-1)

# 2)
change_positive = 0
update_index = 0
for i in range(0,len(profit_loss)-1):
    diff = profit_loss[i+1] - profit_loss[i]
    if diff > change_positive:
        change_positive = diff
        update_index = i+1

greatest_increase_change = (timeframe[update_index],change_positive)

# 3) 
change_negative = 0
update_index = 0
for i in range(0,len(profit_loss)-1):
    diff = profit_loss[i+1] - profit_loss[i]
    if diff < change_negative:
        change_negative = diff
        update_index = i+1

greatest_decrease_change = (timeframe[update_index],change_negative)

with open('analysis/budget.txt','w') as file:
    file.write('Financial Analysis\n')
    file.write("----------------------\n")
    file.write("Total Months: {}\n".format(len(timeframe)))
    file.write("Total: ${}\n".format(sum(profit_loss)))
    file.write("Average  Change: ${}\n".format(avg_change))
    file.write("Greatest Increase in Profits: {} (${})\n".format(greatest_increase_change[0],greatest_increase_change[1]))
    file.write("Greatest Decrease in Profits: {} (${})\n".format(greatest_decrease_change[0],greatest_decrease_change[1]))
    file.close()
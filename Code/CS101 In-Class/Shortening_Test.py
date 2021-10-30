import csv ; player_dict = {} ; file = open("player_info.csv", 'r') ; csvreader = csv.reader(file, delimiter = ',') ; rows = []
for row in csvreader:
    rows.append(row)
for i in range (1, len(rows)):
    player_dict[rows[i][3]] = rows[i]
print(player_dict)
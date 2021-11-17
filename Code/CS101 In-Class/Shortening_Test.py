import csv
player_dict = {}
file = open("player_info.csv", 'r')
csvreader = csv.reader(file, delimiter = ',')
rows = []
for row in csvreader:
    rows.append(row)
for i in range (0, len(rows)):
    player_dict[rows[i][3]] = rows[i]
while True:
    print('R-Roster \nP-Player Ranking by Position \nU-Update a Player\'s ranking \nD-Delete a Player \nT-Top Players \nQ-Quit')
    try:
        ui=input('Choose: \n')
        ui=ui.lower()
        if ui=='r':
            for js in z:
                print(z[js][2],z[js][0],z[js][3],z[js][4])
        elif ui=='p':
            po=input('Position:\n')
            nop=int(input('# players:\n'))
            sort_pd=sorted(z.items(),key=lambda x:int(x[1][4]))
            o=0
            for i in sort_pd:
                if po==i[1][0] and o<nop:
                    print('Name: ',i[1][2],'Position: ',i[1][0],'Jeresy #: ',i[1][3],'Rank: ',i[1][4],'\n');o+=1
        elif ui=='u':
            pn=input('Jeresy #:\n')
            nr=(input('New ranking:\n'))
            if pn in z:
                z[pn][4]=nr
                print('Jeresy',pn,'is now ranked at',nr)
            else:
                print('# not found.\n')
        elif ui=='d':
            pn=input('Jeresy #:\n')
            if pn in z:
                del z[pn]
                print(pn,'has been deleted.')
            else:
                print('# not found.\n')
        elif ui=='t':
            g=int(input('Min ranking:\n'))
            print('Players rated over',g)
            for s in z:
                if int(z[s][4])>=g:
                    print(z[s][2],z[s][0],z[s][3],z[s][4],'\n')
        elif ui=='q':
            quit()
    except:
        print('Invalid input.')






















'''
Before Shortening: 67 Lines

1) Deleting functions and placing within if ladder
2) Reformatting menu and deleting whitespace
3) Use of ; operator in lines that do not require immediate formatting or indentation
4) Use of built-in exec() function within Python to format indented statements
5) Renaming of variables to shorten line lengths

After Shortening: 37 Lines
'''

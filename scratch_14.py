print("\033[0;33;48m╦ ╦┌─┐┬  ┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐\
\n║║║├┤ │  │  │  │ ││││├┤    │ │ │\
\n╚╩╝└─┘┴─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘\033[m")
print("\033[0;36;48m██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ \
\n██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗\
\n██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝\
\n██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ \
\n██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     \
\n╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝ \n")
username=input('Please enter your Name: ')
print(38*'\033[0;30;47m=-\033[m')
pcname='\033[0;35;48m'+'Pc'
#[[linha0[coluna0, coluna1, coluna2],linha1[coluna0, coluna1, coluna2]]
V1=[['~','~','~','~','~','~','~','~','~','~','~','~'],['~','~','~','~','~','~','~','~','~','~','~','~'],['~','~','~','~','~','~','~','~','~','~','~','~'],['~','~','~','~','~','~','~','~','~','~','~','~'],['~','~','~','~','~','~','~','~','~','~','~','~'],['~','~','~','~','~','~','~','~','~','~','~','~'],['~','~','~','~','~','~','~','~','~','~','~','~'],['~','~','~','~','~','~','~','~','~','~','~','~'],['~','~','~','~','~','~','~','~','~','~','~','~'],['~','~','~','~','~','~','~','~','~','~','~','~'],['~','~','~','~','~','~','~','~','~','~','~','~'],['~','~','~','~','~','~','~','~','~','~','~','~']]
H1=['A','B','C','D','E','F','G','H','I','J','K','L']
V2=[['?','?','?','?','?','?','?','?','?','?','?','?'],['?','?','?','?','?','?','?','?','?','?','?','?'],['?','?','?','?','?','?','?','?','?','?','?','?'],['?','?','?','?','?','?','?','?','?','?','?','?'],['?','?','?','?','?','?','?','?','?','?','?','?'],['?','?','?','?','?','?','?','?','?','?','?','?'],['?','?','?','?','?','?','?','?','?','?','?','?'],['?','?','?','?','?','?','?','?','?','?','?','?'],['?','?','?','?','?','?','?','?','?','?','?','?'],['?','?','?','?','?','?','?','?','?','?','?','?'],['?','?','?','?','?','?','?','?','?','?','?','?'],['?','?','?','?','?','?','?','?','?','?','?','?']]
ships=['Carrier (6)','Battleship (5)','Destroyer (4)','Submarine (3)','Patrol Boat (2)']
ship='\033[0;37;44m'+'■'
pcship='■'
usercolor = '\033[0;30;44m '
pccolor ='\033[0;30;43m '
from random import randint
def drawboard(board,color,name):
    z=0
    print()
    print('\033[0;32;48m'+name+"'s Board\033[m")
    print('  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |1 0|1 1|1 2|')
    for abc in board:
        print(H1[z],end=' ')
        z=z+1
        for dot in abc:
            if dot == 'X':
                print('|'+'\033[0;30;41m '+dot+' \033[m',end='')
            else:
                print('|'+color+dot,'\033[m',end='')
        print('|')
#drawboard(V1,usercolor,username)

pc=False
user=True

def getcoordinates(user):
    global V1
    global V2
    a=0
    c=0
    k=6
    for each in ships:
        while True:
            if user:
                drawboard(V1,usercolor,username)
                print()
                print('Now, select the coordinates for the',ships[a],':')
                letter=input('\033[0;35;48m☻ Choose a row (A-L): \033[m').capitalize()
                number=int(input('\033[0;33;48m☺ And a column (1-12): \033[m'))
                letter2=input('\033[0;35;48m☻ Another row: \033[m').capitalize()
                number2=int(input('\033[0;33;48m☺ Another column: \033[m'))
                row=0
                row2=0
                for abcd in H1:
                    if letter==abcd:
                        break
                    row=row+1
                for dots in H1:
                    if letter2==dots:
                        break
                    row2=row2+1
                column=number-1
                column2=number2-1
                if row==row2:
                    for f in range(column,column2+1):
                        V1[row][f]=ship
                elif column==column2:
                    for f in range(row,row2+1):
                        V1[f][column]=ship
                #drawboard(V1,usercolor,username)
                a=a+1
            else:
                colided=False
                hv=randint(0,1)
                pcrow=randint(0,11)
                pccolumn=randint(0,11)
                if hv==0:
                    for c in range(k):
                        if pcrow+k>12:
                            if V2[pcrow-c][pccolumn]==pcship:
                                colided=True
                        else:
                            if V2[pcrow+c][pccolumn]==pcship:
                                colided=True
                    if not colided:
                        for c in range(k):
                            if pcrow+k>12:
                                V2[pcrow-c][pccolumn]=pcship
                            else:
                                V2[pcrow+c][pccolumn]=pcship
                elif hv==1:
                    for c in range(k):
                        if pccolumn+k>12:
                            if V2[pcrow][pccolumn-c]==pcship:
                                colided=True
                        else:
                            if V2[pcrow][pccolumn+c]==pcship:
                                colided=True
                    if not colided:
                        for c in range(k):
                            if pccolumn+k>12:
                                V2[pcrow][pccolumn-c]=pcship
                            else:
                                V2[pcrow][pccolumn+c]=pcship
                if not colided:
                    drawboard(V2,pccolor,pcname)
                    print(ships[a])
                    k=k-1
                    a=a+1
                    break

#getcoordinates(user)
getcoordinates(pc)
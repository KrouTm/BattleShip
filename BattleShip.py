print("\033[0;33;48m╦ ╦┌─┐┬  ┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐\
\n║║║├┤ │  │  │  │ ││││├┤    │ │ │\
\n╚╩╝└─┘┴─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘\033[m")
print("\033[0;36;48m██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ \
\n██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗\
\n██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝\
\n██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ \
\n██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     \
\n╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝ \n")
username=input('Please enter your Name:👉 ')
print(38*'\033[0;30;47m=-\033[m')
pcname='\033[0;35;48m'+'Pc'
H=['A','B','C','D','E','F','G','H','I','J','K','L']
V1=[]
for i in range(12):
    V1.append([' ~']*12)
V2=[]
for i in range(12):
    V2.append([' ?']*12)
ships=['Carrier (6)','Battleship (5)','Destroyer (4)','Submarine (3)','Patrol Boat (2)']
usercolor='\033[0;30;44m'
pccolor='\033[0;30;43m'
ship='\033[0;37;44m'+' ■'
pcship=' ■'
shiphit='\033[0;30;41m X'
waterhit='\033[0;30;46m ~'
from random import randint

def drawboard(board,color,name):#Making the style of the board
    z=0
    print()
    print('\033[0;32;48m'+name+"'s Board\033[m")
    print('  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |1 0|1 1|')
    for abc in board:
        print(H[z],end=' ')
        z=z+1
        for dot in abc:
            print('|'+color+dot,'\033[m',end='')
        print('|')
drawboard(V1,usercolor,username)

def getcoordinatesUser():
    a=0
    for each in ships:
        print()
        #To find out where the user wants to place their boat
        print('Now, select the coordinates for the',ships[a],':')
        letter=input('\033[0;35;48m☻ Choose a row (A-L): \033[m').capitalize()
        number=int(input('\033[0;33;48m☺ And a column (0-11): \033[m'))
        letter2=input('\033[0;35;48m☻ Another row: \033[m').capitalize()
        number2=int(input('\033[0;33;48m☺ Another column: \033[m'))
        #Find out which row and column was chosen by the user
        row=0
        row2=0
        for ABC in H:#Converting letter to number
            if letter==ABC:
                break
            row=row+1
        for ABC in H:#Converting letter to number
            if letter2==ABC:
                break
            row2=row2+1
        #Check if it is on horizontal or vertical
        if letter==letter2:#Horizontal
            for x in range(number,number2+1):#Is adding 1 to the number2 because the range ignores the last number
                V1[row][x]=ship#Replacing the '~' with '■'
        elif number==number2:#Vertical
            for x in range(row,row2+1):#Is adding 1 to the row2 because the range ignores the last number
                V1[x][number]=ship#Replacing the '~' with '■'
        drawboard(V1,usercolor,username)
        a=a+1
getcoordinatesUser()

def getcoordinatesPC():
    k=6
    for ship in ships:#The code must run 5 times as there are five ships
        hv=randint(0,1)
        pcrow=randint(0,11)
        pccolumn=randint(0,11)
        if hv==0:
            for c in range(k):
                if pcrow+k>12:
                    V2[pcrow-c][pccolumn]=pcship#In order not to go over the edge of the board, here we will invert the direction in which the boats will be drawn
                else:
                    V2[pcrow+c][pccolumn]=pcship
        elif hv==1:
            for c in range(k):
                if pccolumn+k>12:
                    V2[pcrow][pccolumn-c]=pcship#In order not to go over the edge of the board, here we will invert the direction in which the boats will be drawn
                else:
                    V2[pcrow][pccolumn+c]=pcship
        k=k-1
getcoordinatesPC()

def Userdropbomb():
    drawboard(V2,pccolor,pcname)
    print()
    #Figuring out where the user wants to put the ships
    print("Enter the coordinates to drop the bomb 💣")
    userletter=input('\033[0;35;48m☻ Choose a row (A-L): \033[m').capitalize()
    usernumber=int(input('\033[0;33;48m☺ And a column (0-11): \033[m'))
    userow=0
    for n in H:
        if userletter==n:
            break
        userow=userow+1
    if V2[userow][usernumber]==pcship:#To update board appearance to ship hit
        V2[userow][usernumber]=shiphit
        drawboard(V2,pccolor,pcname)
        print("Good job patrol! You hit the ship 💪 (•︡益︠•) 👊")
    else:#To update board appearance to water hit
        V2[userow][usernumber]=waterhit
        drawboard(V2,pccolor,pcname)
        print("Not this time, keep trying! ᕦ(ò_óˇ)ᕤ")

def PCdropbomb():
    #Generating a random number in the coordinates of the board
    hh=randint(0,11)
    vv=randint(0,11)
    if V1[hh][vv]==ship:#To update ship appearance to ship hit
        V1[hh][vv]=shiphit
        drawboard(V1,usercolor,username)
        print("PC hit your ship (◡̀_◡́҂)")
    else:#To update board appearance to water hit
        V1[hh][vv]=waterhit
        drawboard(V1,usercolor,username)
        print("PC hit the water (☞ﾟヮﾟ)☞")

game=True
while game:
    Userdropbomb()
    PCdropbomb()
    cont=0
    cont2=0
    for l in V2:
        for d in l:
            if d.find('■') != -1: #Looks for ■ ship symbol in PC's board
                cont=cont+1 #Counts number of ship symbols in PC's board
    if cont==0:
        game=False
        print("\033[0;33;48m █████ █████    ███████    █████  █████    █████   ███   █████ █████ ██████   █████ ███\
        \n░░███ ░░███   ███░░░░░███ ░░███  ░░███    ░░███   ░███  ░░███ ░░███ ░░██████ ░░███ ░███\
        \n ░░███ ███   ███     ░░███ ░███   ░███     ░███   ░███   ░███  ░███  ░███░███ ░███ ░███\
        \n  ░░█████   ░███      ░███ ░███   ░███     ░███   ░███   ░███  ░███  ░███░░███░███ ░███\
        \n   ░░███    ░███      ░███ ░███   ░███     ░░███  █████  ███   ░███  ░███ ░░██████ ░███\
        \n    ░███    ░░███     ███  ░███   ░███      ░░░█████░█████░    ░███  ░███  ░░█████ ░░░ \
        \n    █████    ░░░███████░   ░░████████         ░░███ ░░███      █████ █████  ░░█████ ███\
        \n   ░░░░░       ░░░░░░░      ░░░░░░░░           ░░░   ░░░      ░░░░░ ░░░░░    ░░░░░ ░░░\033[m")
    for l in V1:
        for d in l:
            if d.find('■') != -1: #Looks for ■ ship symbol in User's board
                cont2=cont2+1 #Counts number of ship symbols in User's board
    if cont2==0:
        game=False
        print("\033[0;31;48m █████ █████    ███████    █████  █████    █████          ███████     █████████  ██████████ ███\
        \n░░███ ░░███   ███░░░░░███ ░░███  ░░███    ░░███         ███░░░░░███  ███░░░░░███░░███░░░░░█░███\
        \n ░░███ ███   ███     ░░███ ░███   ░███     ░███        ███     ░░███░███    ░░░  ░███  █ ░ ░███\
        \n  ░░█████   ░███      ░███ ░███   ░███     ░███       ░███      ░███░░█████████  ░██████   ░███\
        \n   ░░███    ░███      ░███ ░███   ░███     ░███       ░███      ░███ ░░░░░░░░███ ░███░░█   ░███\
        \n    ░███    ░░███     ███  ░███   ░███     ░███      █░░███     ███  ███    ░███ ░███ ░   █░░░\
        \n    █████    ░░░███████░   ░░████████      ███████████ ░░░███████░  ░░█████████  ██████████ ███\
        \n   ░░░░░       ░░░░░░░      ░░░░░░░░      ░░░░░░░░░░░    ░░░░░░░     ░░░░░░░░░  ░░░░░░░░░░ ░░░ \033[m")
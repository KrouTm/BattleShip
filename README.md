# BattleShip

THE GAME WILL ONLY WORK PERFECTLY ON PYCHARM OR LINUX (SOME PLATAFORM THAT SUPPORTS RICHTEXT).

BOARD
 
- The first thing I started doing was the board.
 
- Notice that when the user writes the name, it appears just above the board saying the user's own name instead of "Your board" for example", this makes the game more inviting for the user.
 
- In the beginning the board was written in an extensive form, very long, as "V1=[' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~' ,' ~',' ~',' ~',' ~']", this was written 12 times and the code did not work as it should if I put for example "V1=[' ~'* 12]* 12" or "V1=[' ~',' ~',' ~',' ~',' ~',' ~',' ~',' ~' ,' ~',' ~',' ~',' ~' ] * 12", because the language interprets this as being the same element, the ' ~' should be considered as an individual element, but after some trial and error I was able to change it to:
"V1=[]
for i in range(12):
	V1.append([' ~'] * 12)"
   
- And in case it wasn't very clear, the spaces at the beginning of the '~' are just to give it a better appearance and to be able to color the background of one of the ' ~' to red replacing it with 'X' when both players throw the bomb and manage to hit a part of the ship.
 
GETTING THE USERS COORDINATES
 
- Instructions were placed for the user to be able to insert the coordinates where he wants to insert the ship.
 
- Here "letter=input('\0330;35;48m☻ Choose a row (AL): \033m').capitalize()" and here "letter2=input('\0330;35;48m☻ Another row: \ 033m').capitalize()", it was necessary to transform the letter in which the user typed into a number. That's why it was necessary to capitalize the input letter to be able to compare the letters of "H=['A','B','C','D','E','F','G','H' ,'I','J','K','L']") and "turn into number" with for loop.
 
- There were flaws such as: the user can input wrong coordinates, the code does not detect the error and does not offer a chance to try again, if the user inputs all the coordinates correctly in the first four ships and in the fifth ship the user makes a mistake, he will have to restart the game and enter the data again, but now the code detects the some errors and offer to write it again, There would have to be codes to detect when the user places an '■' (in this case a piece of the boat) on top of another '■', in case the user misses the row or column where he would put the rest of the boat, when the user writes a letter or number or any other type of character that does not exist in the board options, etc.
 
- Besides the bugs it is not clear enough how exactly the user should place the boats, the user must understand that the Carrier is six '■' consecutively without separating one '■' from the other '■', like '■ ■ ■ ■ ■ ■', it should look like this on the board, but I couldn't think of a better way to express this without using another platform, just using pure python.
 
GETTING THE PC COORDINATES
 
- Randint property of random was used to choose a random number. The variable "hv=randint(0,1)" means that it will randomly choose 0 or 1 with the intention of defining whether the boat will be drawn horizontally or vertically:

■ or ■ ■ ■ ■ ■ ■

■

■

■

■

■
 
- "pcrow=randint(0,11)" and "pccolumn=randint(0,11)" is also randomly choosing a number from 0 to 11 because there are 12 rows and 12 columns (columns represented by the variable "H=['A ','B','C','D','E','F','G','H','I','J','K','L']").
 
- Just below in the for loop I'm replacing the '~' that represents the water by '■' that represents the ship. However, before being printed, the program can detect if the ship exceeds the board and a part of the ship will not be printed within the area of the board. If this happens, it will print it in the opposite direction, that is, negatively. This was one of the initial problems of this part, it took a lot of effort to find a way for the ship not to be printed before knowing if it would fit, before that was solved the program would print the part of the ship that fit on the board and not print the rest.
 
- There is also a problem where the program does not detect if the ships will collide (one ship or more being printed in the same place) this also happens with getcoordinatesUser. I tried several ways to correct this, because it is a problem that also affects the number of '■' inside the board and with that, if there is not the exact number of '■', it will not be possible to fairly declare a winner or loser.
 
- The program does not have artificial intelligence in case it hits an '■' and keeps trying in the same area until it finishes destroying the entire ship for example. It may happen that the program may reach the same place where it had already reached before. So issu makes him a practically irrelevant opponent hahaha, being almost impossible for him to beat the user.
 
- I could try to fix this but it would take a lot of time and my deadline is only one month, as just a beginner this is difficult.
 
WHEN THE USER WILL THROW THE BOMB

- The idea is very similar to when the user chooses where to place the '■', there was no fanfare with that. Add some comments so the player can think about fun instead of thinking I can have more time to comment more on what the computer can randomly pick one of them.

WHEN THE PC WILL THROW THE BOMB

- Also being a simple idea when the PC randomly chooses a redder place on the board to place the bars, this function randomly chooses a place to place the "X" with background indicating that the boat has been hit.

WHILE LOOP

- The while loop is designed so that it prints and executes the above functions when it ends with a winner and loser breaking the loop. The biggest difficulty in this part was finding a way to count '■', because whoever gets 20*'■' first wins. Everything was solved with the variable.find() function.

SOME GAME SCREENSHOTS ON PYCHARM
![alt text](https://github.com/KrouTm/BattleShip/blob/main/screenshots/game.PNG?raw=true)
![alt text](https://github.com/KrouTm/BattleShip/blob/main/screenshots/game2.PNG?raw=true)
![alt text](https://github.com/KrouTm/BattleShip/blob/main/screenshots/game3.PNG?raw=true)
![alt text](https://github.com/KrouTm/BattleShip/blob/main/screenshots/game4.PNG?raw=true)

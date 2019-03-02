import os
import random
import platform
import sys


#print colored('hello', 'red'), colored('world', 'green')
#print("\033[1;32;40m Bright Green  \n")
#sys.stdout.write('\a')
#sys.stdout.flush()


try:
    from msvcrt import getch #For windows
except ImportError: 
    def getch():
    
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def pressedkey():
	return getch()


stuff  = {'wall'  :  u"\033[1;34;44m\u2588",
					'player':  "\033[1;32;46m@",
					'empty' :  "\033[0;36;46m.",
					'enemy' :  "\033[1;31;46me",
          'money' :  "$",
          'chest' :  "C"}


room = {1:[stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall']], # ^
	    2:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
	    3:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
	    4:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
	    5:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['player'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
	    6:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # x
	    7:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
	    8:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
	    9:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
			10:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
			11:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
			12:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
			13:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
			14:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
			15:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
			16:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
			17:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
			18:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['enemy'],stuff['empty'],stuff['enemy'],stuff['empty'],stuff['enemy'],stuff['empty'],stuff['enemy'],stuff['empty'],stuff['enemy'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
			19:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
			20:[stuff['wall'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['empty'],stuff['wall']], # |
	   21:[stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall'],stuff['wall']]} # |
	    # <------------------------------y--------------------------------->

#potion = ['hp','xp','dmg']
#weapon = ['sword','nuclear bomb','TNT']


	

pos = [] # 0 is X,1 is Y
enemy_pos = []
player_flag = 0
player_health = 100
enemy_health = 10 
dragon_health = 50

def enemy_move():
	for i in range(1,len(room)+1):
		if stuff['enemy'] in room[i]:
			x_axis = i
			y_axis = room[i].index(stuff['enemy'])
			del enemy_pos[:]
			enemy_pos.append(x_axis)
			enemy_pos.append(y_axis)
			move = random.randint(1, 4)
			if move == 1 and room[enemy_pos[0]-1][enemy_pos[1]] is stuff['empty']:
				up(room,stuff['empty'],stuff['enemy'],enemy_pos)
			elif move == 2 and room[enemy_pos[0]+1][enemy_pos[1]] is stuff['empty']:
				 down(room,stuff['empty'],stuff['enemy'],enemy_pos)
			elif move == 3 and room[enemy_pos[0]][enemy_pos[1]-1] is stuff['empty']:
				 left(room,stuff['empty'],stuff['enemy'],enemy_pos)
			elif move == 4 and room[enemy_pos[0]][enemy_pos[1]+1] is stuff['empty']:
				 right(room,stuff['empty'],stuff['enemy'],enemy_pos)
			check_pos(room,enemy_pos)
		  

def gamemap():
    for i in range(1,len(room)+1):
	    print ("".join(room[i]))


def player_pos():
    for i in range(1,len(room)+1):
      if stuff['player'] in room[i]:
        x_axis = i
        y_axis = room[i].index(stuff['player'])
        del pos[:]
        pos.append(x_axis)
        pos.append(y_axis)
        

def updater():
	if platform.system() =='Windows':
		os.system('cls')
	elif platform.system() == 'Linux':
		os.system('clear') 
		#print('\n'*5)
	gamemap()
	print("\033[1;37;40m")
	#os.system('setterm -background default -foreground default')
	player_pos()

def check_pos(mdictionary,mcoordinates): 
	if mdictionary[mcoordinates[0]-1][mcoordinates[1]] == stuff['player']: 
		print(mcoordinates)
		fight()
	if mdictionary[mcoordinates[0]+1][mcoordinates[1]] == stuff['player']: 
		print(mcoordinates)
		fight()
	if mdictionary[mcoordinates[0]][(mcoordinates[1]+1)] == stuff['player']: 
		print(mcoordinates)
		fight()
	if mdictionary[mcoordinates[0]][(mcoordinates[1]-1)] == stuff['player']: 
		print(mcoordinates)
		fight()



def up(dictionary,inst_replace,inst_player,coordinates):
	(dictionary[coordinates[0]]).pop(coordinates[1])
	(dictionary[coordinates[0]]).insert(coordinates[1],inst_replace)
	(dictionary[coordinates[0]-1]).pop(coordinates[1])
	(dictionary[coordinates[0]-1]).insert(coordinates[1],inst_player)
	coordinates[0:1] = [coordinates[0]-1,coordinates[1]]
	
	if player_flag == 1: updater()
	#check_pos(dictionary,coordinates)


def down(dictionary,inst_replace,inst_player,coordinates):
	(dictionary[coordinates[0]]).pop(coordinates[1])
	(dictionary[coordinates[0]]).insert(coordinates[1],inst_replace)
	(dictionary[coordinates[0]+1]).pop(coordinates[1])
	(dictionary[coordinates[0]+1]).insert(coordinates[1],inst_player)
	coordinates[0:1] = [coordinates[0]+1,coordinates[1]]
	if player_flag == 1: updater()
	#check_pos(dictionary,coordinates)

def left(dictionary,inst_replace,inst_player,coordinates):
	(dictionary[coordinates[0]]).pop(coordinates[1])
	(dictionary[coordinates[0]]).insert(coordinates[1],inst_replace)
	(dictionary[coordinates[0]]).pop(coordinates[1]-1)
	(dictionary[coordinates[0]]).insert(coordinates[1]-1,inst_player)
	coordinates[0:1] = [coordinates[0],coordinates[1]-1]
	if player_flag == 1: updater()
	#check_pos(dictionary,coordinates)

def right(dictionary,inst_replace,inst_player,coordinates):
	(dictionary[coordinates[0]]).pop(coordinates[1])
	(dictionary[coordinates[0]]).insert(coordinates[1],inst_replace)
	(dictionary[coordinates[0]]).pop(coordinates[1]+1)
	(dictionary[coordinates[0]]).insert(coordinates[1]+1,inst_player)
	coordinates[0:1] = [coordinates[0],coordinates[1]+1]
	if player_flag == 1: updater()
	#check_pos(dictionary,coordinates)

def fight():
  print("You encountered: enemy")
  print("What will you do?\n1: Fight\n2: Run Away\n")


updater()

while True:
	pressedkey = getch()
	if pressedkey is 'w' or pressedkey is 'W':
		if room[pos[0]-1][pos[1]] is not stuff['wall']:
			up(room, stuff['empty'], stuff['player'],pos)
			player_flag = 1
			enemy_move()
			player_flag = 0
			#updater()
			print("HP: " + str(player_health))
		else:
			enemy_move()
			updater()
	elif pressedkey is 's' or pressedkey is 'S':
		if room[pos[0]+1][pos[1]] is not stuff['wall']:
			down(room,stuff['empty'],stuff['player'],pos)
			player_flag = 1
			enemy_move()
			player_flag = 0
			#updater()
			print("HP: " + str(player_health))
		else:
			player_flag = 1
			enemy_move()
			player_flag = 0
	elif pressedkey is 'a' or pressedkey is 'A':
		if room[pos[0]][pos[1]-1] is not stuff['wall']:
			left(room,stuff['empty'], stuff['player'],pos)
			player_flag = 1
			enemy_move()
			player_flag = 0
			#updater()
			print("HP: " + str(player_health))
		else:
			player_flag = 1
			enemy_move()
			player_flag = 0
	elif pressedkey is 'd' or pressedkey is 'D':
		if room[pos[0]][pos[1]+1] is not stuff['wall']:
			right(room,stuff['empty'], stuff['player'],pos)
			player_flag = 1
			enemy_move()
			player_flag = 0
			#updater()
			print("HP: " + str(player_health))
		else:
			player_flag = 1
			enemy_move()
			player_flag = 0
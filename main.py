#HAkron 4K: The Game
# Copyright (c) Saikishore Gowrishankar
# Any trademarks used in this program belong to their respective owners. Lawyers love tautologies.

import os
import random
import platform
import sys
import time
import readchar

pos = [] # 0 is X,1 is Y
player_flag = 0
player_health = 100
gold_available = 5
potions = [0,0,0]

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
    
print(u"Welcome to...\n")
print("██╗  ██╗ █████╗ ██╗  ██╗██████╗  ██████╗ ███╗   ██╗    ██╗  ██╗██╗  ██╗ ")
print("██║  ██║██╔══██╗██║ ██╔╝██╔══██╗██╔═══██╗████╗  ██║    ██║  ██║██║ ██╔╝██╗")
print("███████║███████║█████╔╝ ██████╔╝██║   ██║██╔██╗ ██║    ███████║█████╔╝ ╚═╝")
print("██╔══██║██╔══██║██╔═██╗ ██╔══██╗██║   ██║██║╚██╗██║    ╚════██║██╔═██╗ ██╗")
print("██║  ██║██║  ██║██║  ██╗██║  ██║╚██████╔╝██║ ╚████║         ██║██║  ██╗╚═╝")
print("╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝         ╚═╝╚═╝  ╚═╝   ")

print("\n")

print("████████╗██╗  ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗         ")
print("╚══██╔══╝██║  ██║██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝         ")
print("   ██║   ███████║█████╗      ██║  ███╗███████║██╔████╔██║█████╗           ")
print("   ██║   ██╔══██║██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝           ")
print("   ██║   ██║  ██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗         ")
print("   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝         ")

print("Press any key to continue...")

temp_key = getch()


stuff  = {'wall'  :  u"\033[1;33;43m\u2588",
					'player':  u"\033[1;32;44m@",
					'empty' :  u"\033[0;34;44m.",
					'enemy' :  u"\033[1;31;44me",
					'dead'  :  u"\033[1;31;44mX",
          'vendor':  u"\033[1;37;40mV",} #u"C"

class Inventory:
    items = []
inventory_i = Inventory()


class Map:
	room = {1:[stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"]], # ^
				 2:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
			 	 3:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				 4:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				 5:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				 6:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # x
				 7:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				 8:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				 9:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["enemy"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["vendor"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				10:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				11:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				12:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["player"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				13:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				14:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				15:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				16:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				17:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				18:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["enemy"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |
				19:[stuff["wall"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["empty"],stuff["wall"]], # |# |
			20:[stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"],stuff["wall"]]} # |
	def gamemap(self):
		for i in range(1,len(self.room)+1):
			print ("".join(self.room[i]))
	def updater(self):
		if platform.system() =='Windows':
			os.system('cls')
		elif platform.system() == 'Linux':
			os.system('clear') 
		self.gamemap()
		print("\033[1;37;40m")
		player_pos()
	def check_pos(self,mdictionary,mcoordinates): 
		if mdictionary[mcoordinates[0]-1][mcoordinates[1]] == stuff['player']: 
			fight("up")
		if mdictionary[mcoordinates[0]+1][mcoordinates[1]] == stuff['player']: 
			fight("down")
		if mdictionary[mcoordinates[0]][(mcoordinates[1]+1)] == stuff['player']: 
			fight("right")
		if mdictionary[mcoordinates[0]][(mcoordinates[1]-1)] == stuff['player']: 
			fight("left")
			
map_i = Map()
#potion = ['hp','xp','dmg']
#weapon = ['sword','nuclear bomb','TNT']

class Enemy:
	enemy_pos = []
	enemy_health = 10 
	enemy_names = ["Wendigo", "Kuloscap", "Asura", "Rakshasa", "Leviathan", "Rugaru", "Sephiroth", "Vajra", "Hitobashira", "Jörmungandr"]
	def enemy_move(self):
		for i in range(1,len(map_i.room)+1):
			if stuff['enemy'] in map_i.room[i]:
				x_axis = i
				y_axis = map_i.room[i].index(stuff['enemy'])
				del self.enemy_pos[:]
				self.enemy_pos.append(x_axis)
				self.enemy_pos.append(y_axis)
				move = random.randint(1, 4)
				if move == 1 and map_i.room[self.enemy_pos[0]-1][self.enemy_pos[1]] is stuff['empty']:
					up(map_i.room,stuff['empty'],stuff['enemy'],self.enemy_pos)
				elif move == 2 and map_i.room[self.enemy_pos[0]+1][self.enemy_pos[1]] is stuff['empty']:
					down(map_i.room,stuff['empty'],stuff['enemy'],self.enemy_pos)
				elif move == 3 and map_i.room[self.enemy_pos[0]][self.enemy_pos[1]-1] is stuff['empty']:
					left(map_i.room,stuff['empty'],stuff['enemy'],self.enemy_pos)
				elif move == 4 and map_i.room[self.enemy_pos[0]][self.enemy_pos[1]+1] is stuff['empty']:
					right(map_i.room,stuff['empty'],stuff['enemy'],self.enemy_pos)
				map_i.check_pos(map_i.room,self.enemy_pos)
		map_i.updater()
	
enemy_i = Enemy()


def vendor():
    global player_health
    global gold_available
    global potions
    print("Welcome Adventurer to my humble shop!\nI offer a great many things, like:\n1: A small health potion (+20 HP), 15 gold\n2: A medium health potion (+50 HP), 30 gold\n3: A health restorer (100% HP), 50 gold\n")
    option = input("")
    if option == '1':
        price = 15
        player_health += 20
        if player_health > 100: player_health = 100
    elif option == '2':
        price = 30
        player_health += 50
        if player_health > 100: player_health = 100
    elif option == '3':
        price = 50
        player_health = 100
    else:
        print("My apologies, foreigner. I do not speak your tongue.")
        test = getch()
        return
    if price > gold_available:
        print("BEGGAR! BEGONE WITH YOUR WRETCHED FILTH!")
    else:
        gold_available -= price
        potions[int(option)-1] += 1
        if option == '1' or option == '2' or option == '3':
            print("Thank you for you patronage!")
        else:
        	print("My apologies, foreigner. I do not speak your tongue.")

def player_pos():
    for i in range(1,len(map_i.room)+1):
      if stuff['player'] in map_i.room[i]:
        x_axis = i
        y_axis = map_i.room[i].index(stuff['player'])
        del pos[:]
        pos.append(x_axis)
        pos.append(y_axis)

def up(dictionary,inst_replace,inst_player,coordinates):
	(dictionary[coordinates[0]]).pop(coordinates[1])
	(dictionary[coordinates[0]]).insert(coordinates[1],inst_replace)
	(dictionary[coordinates[0]-1]).pop(coordinates[1])
	(dictionary[coordinates[0]-1]).insert(coordinates[1],inst_player)
	coordinates[0:1] = [coordinates[0]-1,coordinates[1]]
	
	#if player_flag == 1: map_i.updater()
	#map_i.check_pos(dictionary,coordinates)


def down(dictionary,inst_replace,inst_player,coordinates):
	(dictionary[coordinates[0]]).pop(coordinates[1])
	(dictionary[coordinates[0]]).insert(coordinates[1],inst_replace)
	(dictionary[coordinates[0]+1]).pop(coordinates[1])
	(dictionary[coordinates[0]+1]).insert(coordinates[1],inst_player)
	coordinates[0:1] = [coordinates[0]+1,coordinates[1]]
	#if player_flag == 1: map_i.updater()
	#map_i.check_pos(dictionary,coordinates)

def left(dictionary,inst_replace,inst_player,coordinates):
	(dictionary[coordinates[0]]).pop(coordinates[1])
	(dictionary[coordinates[0]]).insert(coordinates[1],inst_replace)
	(dictionary[coordinates[0]]).pop(coordinates[1]-1)
	(dictionary[coordinates[0]]).insert(coordinates[1]-1,inst_player)
	coordinates[0:1] = [coordinates[0],coordinates[1]-1]
	#if player_flag == 1: map_i.updater()
	#map_i.check_pos(dictionary,coordinates)

def right(dictionary,inst_replace,inst_player,coordinates):
	(dictionary[coordinates[0]]).pop(coordinates[1])
	(dictionary[coordinates[0]]).insert(coordinates[1],inst_replace)
	(dictionary[coordinates[0]]).pop(coordinates[1]+1)
	(dictionary[coordinates[0]]).insert(coordinates[1]+1,inst_player)
	coordinates[0:1] = [coordinates[0],coordinates[1]+1]
	#if player_flag == 1: map_i.updater()
	#map_i.check_pos(dictionary,coordinates)

def fight(direction):
	enemy_name = random.choice(enemy_i.enemy_names)
	map_i.updater()
	print("You encountered: " + enemy_name)
	get_press = input("What will you do?\n1: Fight\n2: Run Away\n")
	if get_press == "1" :
		global player_health 
		while player_health > 0:
			#global enemy_i.enemy_health
			global gold_available
			c = random.randint(2,5)
			b = random.randint(6,10)
			gold_drop = random.randint(5,15)
			print("You attacked " + enemy_name + " with damage of: " + str(c))
			enemy_i.enemy_health -= c
			getch()
			if enemy_i.enemy_health <= 0 : 
				enemy_i.enemy_health = 0
				print(enemy_name + " died!")
				enemy_i.enemy_health = 10
				gold_available += gold_drop
				dummy_key = getch()
				player_pos()
				if direction == "up" : down(map_i.room,stuff['empty'],stuff['player'],pos)
				if direction == "down" : up(map_i.room,stuff['empty'],stuff['player'],pos)
				if direction == "left" : right(map_i.room,stuff['empty'],stuff['player'],pos)
				if direction == "right" : left(map_i.room,stuff['empty'],stuff['player'],pos)
				break
			print(enemy_name + " attacked with damage of: " + str(b))
			player_health -= b
			getch()
	
	if get_press == "2" : 
			sub = random.choice([0,random.randint(5,random.randint(10,30))])
			if sub == 0 : print("You escaped suffering no damage!")
			else : print("You escaped suffering " + str(sub) + " damage")
			getch()
			player_health -= sub
			if player_health <= 0: player_health = 0
			map_i.updater()
			print("HP: " + str(player_health))
			print("Gold: " + str(gold_available))
			
map_i.updater()

def inventory():
	global potions
	global player_health
	if platform.system() == 'Windows': os.system('cls')
	elif platform.system() == 'Linux': os.system('clear')
	print("INVENTORY:")
	print("1.) Small Potions: " + str(potions[0]))
	print("2.) Medium Potions: " + str(potions[1]))
	print("3.) Health Restorer: " + str(potions[2]))
	t = getch()
while True:
	if player_health <= 0 : break
	pressedkey = getch()
	print(pressedkey)
	if pressedkey is b'i' or pressedkey is 'i': inventory()
	if pressedkey is b'w' or pressedkey is 'w':
		if map_i.room[pos[0]-1][pos[1]] is stuff['enemy']:
			map_i.updater()
			fight("down")
		if map_i.room[pos[0]-1][pos[1]] is stuff['vendor']:
			map_i.updater()
			vendor()
		elif map_i.room[pos[0]-1][pos[1]] is stuff['empty']:
			up(map_i.room, stuff['empty'], stuff['player'],pos)
			player_flag = 1
			enemy_i.enemy_move()
			player_flag = 0
			map_i.updater()
			print("HP: " + str(player_health))
			print("Gold: " + str(gold_available))
		else:
			enemy_i.enemy_move()
			map_i.updater()
	elif pressedkey is b's' or pressedkey is 's':
		if map_i.room[pos[0]+1][pos[1]] is stuff['enemy']:
			map_i.updater()
			fight("up")
		if map_i.room[pos[0]+1][pos[1]] is stuff['vendor']:
			map_i.updater()
			vendor()
		elif map_i.room[pos[0]+1][pos[1]] is stuff['empty']:
			down(map_i.room,stuff['empty'],stuff['player'],pos)
			player_flag = 1
			enemy_i.enemy_move()
			player_flag = 0
			map_i.updater()
			print("HP: " + str(player_health))
			print("Gold: " + str(gold_available))
		else:
			player_flag = 1
			enemy_i.enemy_move()
			player_flag = 0
	elif pressedkey is b'a' or pressedkey is 'a':
		if map_i.room[pos[0]][pos[1]-1] is stuff['enemy']:
			map_i.updater()
			fight("right")
		if map_i.room[pos[0]][pos[1]-1] is stuff['vendor']:
			map_i.updater()
			vendor()
		elif map_i.room[pos[0]][pos[1]-1] is stuff['empty']:
			left(map_i.room,stuff['empty'], stuff['player'],pos)
			player_flag = 1
			enemy_i.enemy_move()
			player_flag = 0
			map_i.updater()
			print("HP: " + str(player_health))
			print("Gold: " + str(gold_available))
		else:
			player_flag = 1
			enemy_i.enemy_move()
			player_flag = 0
	elif pressedkey is b'd' or pressedkey is 'd':
		if map_i.room[pos[0]][pos[1]+1] is stuff['enemy']:
			map_i.updater()
			fight("left")
		if map_i.room[pos[0]][pos[1]+1] is stuff['vendor']:
			map_i.updater()
			vendor()
		elif map_i.room[pos[0]][pos[1]+1] is stuff['empty']:
			right(map_i.room,stuff['empty'], stuff['player'],pos)
			player_flag = 1
			enemy_i.enemy_move()
			player_flag = 0
			map_i.updater()
			print("HP: " + str(player_health))
			print("Gold: " + str(gold_available))
		else:
			player_flag = 1
			enemy_i.enemy_move()
			player_flag = 0

map_i.room[pos[0]][pos[1]] = stuff["dead"]
print(u"\033[1;32;41m.")
map_i.updater()
print("GAME OVER. Press 'e' to exit")
deadkey = getch()
while (deadkey != b'e' and deadkey != 'e'): deadkey = getch()

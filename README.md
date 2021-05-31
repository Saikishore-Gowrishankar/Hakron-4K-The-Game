# Hakron-4K-The-Game
![HAkron 4K: The Game](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/856/597/datas/original.PNG)

# Inspiration
This project was created to simulate the style of games created in the late 70s and 80s, similar to the video game "Rogue". It is implemented without the use of any external graphics rendering library and the game is rendered entirely through ASCII characters in the command prompt. 

# The Game
The player (@) is spawned in a hardcoded map with various enemy characters (e). The enemies will move around the map (pseudo)randomly. When the player encounters an enemy, the player will initiate a traditional RPG-style battle sequence, where the player and the enemy exchange attacks. Defeating an enemy will drop a certain amount of gold, which can be used at to buy health potions from the vender (V). The current goal of the game is to defeat all the enemies on the screen. The enemies have names that are randomly selected from a hardcoded list.

# Future directions

Future work on this project may lead to a fully functioning inventory system, and an AI system for the enemies to chase the player when within a particular radius. Future work may also look into algorithms for maze generation as well as a more robust and efficient method for printing ASCII characters to the screen (such as the ncurses library in C). 

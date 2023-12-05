# You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

# The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

# As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

# You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

# For example, the record of a few games might look like this:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

import re

file_path = "Day 2/game_text.txt"

max_red= 12
max_green= 13
max_blue= 14

red_counter=0
green_counter= 0
blue_counter= 0



with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()
    words= file_contents.splitlines()
    

def game_possibility_check(lst, color):
    for num in lst:
        if color == 'red' and num > max_red:
            return False
        elif color == 'green' and num > max_green:
            return False
        elif color == 'blue' and num > max_blue:
            return False
    return True


for word in words:
    game_name_split, elf_pick_split=word.split(": ")            # Splits the Game # from the rest of the sentence
    elf_pick_split=elf_pick_split.split(";")                    # Splits the rest of the sentence into each color and their amount
    game_id_split= game_name_split.split(" ")                   # Splits word Game from the number
    game_id= int(game_id_split[1])                              # Converts the game ID into an integer
    
    """Grabbing number of each color."""
    red_color_amount= [int(x) for x in re.findall(r'(\d+(?:\.\d+)?) red', word)]
    blue_color_amount= [int(x) for x in re.findall(r'(\d+(?:\.\d+)?) blue', word)]
    green_color_amount= [int(x) for x in re.findall(r'(\d+(?:\.\d+)?) green', word)]
    
    """Converting list to integer."""
    for num in range(0, len(red_color_amount)):
        red_color_amount[num]= int(red_color_amount[num])
        possibility_red= game_possibility_check(red_color_amount, 'red')
    for num in range(0, len(blue_color_amount)):
        blue_color_amount[num]= int(blue_color_amount[num])
        possibility_blue= game_possibility_check(blue_color_amount, 'blue')
    for num in range(0, len(green_color_amount)):
        green_color_amount[num]= int(green_color_amount[num])
        possibility_green= game_possibility_check(green_color_amount, 'green')
        
    if possibility_red == 'False':
        print("Sorry. Can't do that.")
    else:
        print("Ok!")
    
    if possibility_green == 'False':
        print("Sorry. Can't do that.")
    else:
        print("Ok!")
        
    if possibility_blue == 'False':
        print("Sorry. Can't do that.")
    else:
        print("Ok!")
            
        
    
    

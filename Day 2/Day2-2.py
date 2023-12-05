# --- Part Two ---
# The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

# As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

# Again consider the example games from earlier:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
# Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
# Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
# Game 4 required at least 14 red, 3 green, and 15 blue cubes.
# Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?



import re
file_path = "Day 2/game_text.txt"

max_red= 12
max_green= 13
max_blue= 14
count= 0
power_count= 0



with open(file_path, 'r') as file:
    """Read the contents of the file"""
    file_contents = file.read()
    words= file_contents.splitlines()
    

def game_possibility_check(list, color):
    """Checks numbers and colors in list against the max amount of colors available and returns True or False."""
    for num in list:
        if color == 'red' and num > max_red:
            return False
        elif color == 'green' and num > max_green:
            return False
        elif color == 'blue' and num > max_blue:
            return False
    return True


def min_calculation():
    pass


for word in words:
    """Start for loop to parse through text."""
    game_name_split, elf_pick_split=word.split(": ")            # Splits the Game # from the rest of the sentence
    elf_pick_split=elf_pick_split.split(";")                    # Splits the rest of the sentence into each color and their amount
    game_id_split= game_name_split.split(" ")                   # Splits word Game from the number
    game_id= int(game_id_split[1])                              # Converts the game ID into an integer
    
    """Grabbing number of each color and converting to integer."""
    red_color_amount= [int(num) for num in re.findall(r'(\d+(?:\.\d+)?) red', word)]
    blue_color_amount= [int(num) for num in re.findall(r'(\d+(?:\.\d+)?) blue', word)]
    green_color_amount= [int(num) for num in re.findall(r'(\d+(?:\.\d+)?) green', word)]
    
    """Checks numbers for green, blue and red to see if it exceeds the max available for each color"""
    possibility_red = game_possibility_check(red_color_amount, 'red')
    possibility_green = game_possibility_check(green_color_amount, 'green')
    possibility_blue = game_possibility_check(blue_color_amount, 'blue')
    
    """Takes results for each of the color possibilities and adds the game ID to the count."""
    if not possibility_red or not possibility_green or not possibility_blue:
        count += 0
        # print(f"Game {game_id} is impossible.")
    else:
        count += game_id
        # print(f"Game {game_id} is possible.")
        
    min_red= max(red_color_amount)
    min_green= max(green_color_amount)
    min_blue= max(blue_color_amount)
    
    power_of_set= min_red*min_green*min_blue
    power_count+= power_of_set
    
    
    # print(f"Game {game_id}: The minimum red needed is {min_red}, the minimum green needed for {min_green}, the minimum blue needed for {min_blue}")     
    # print(f"The power of Game #{game_id} is {power_of_set}")   
     
print(f"The addition of the ID's of all possible games is {count}")
print(f"The total power count is {power_count}")
    
    
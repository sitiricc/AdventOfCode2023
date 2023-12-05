# --- Day 4: Scratchcards ---
# The gondola takes you up. Strangely, though, the ground doesn't seem to be coming with you; you're not climbing a mountain. As the circle of Snow Island recedes below you, an entire new landmass suddenly appears above you! The gondola carries you to the surface of the new island and lurches into the station.

# As you exit the gondola, the first thing you notice is that the air here is much warmer than it was on Snow Island. It's also quite humid. Is this where the water source is?

# The next thing you notice is an Elf sitting on the floor across the station in what seems to be a pile of colorful square cards.

# "Oh! Hello!" The Elf excitedly runs over to you. "How may I be of service?" You ask about water sources.

# "I'm not sure; I just operate the gondola lift. That does sound like something we'd have, though - this is Island Island, after all! I bet the gardener would know. He's on a different island, though - er, the small kind surrounded by water, not the floating kind. We really need to come up with a better naming scheme. Tell you what: if you can help me with something quick, I'll let you borrow my boat and you can go visit the gardener. I got all these scratchcards as a gift, but I can't figure out what I've won."

# The Elf leads you over to the pile of colorful cards. There, you discover dozens of scratchcards, all with their opaque covering already scratched off. Picking one up, it looks like each card has two lists of numbers separated by a vertical bar (|): a list of winning numbers and then a list of numbers you have. You organize the information into a table (your puzzle input).

# As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear in the list of winning numbers. The first match makes the card worth one point and each match after the first doubles the point value of that card.

# For example:

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

# Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
# Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
# Card 4 has one winning number (84), so it is worth 1 point.
# Card 5 has no winning numbers, so it is worth no points.
# Card 6 has no winning numbers, so it is worth no points.
# So, in this example, the Elf's pile of scratchcards is worth 13 points.

# Take a seat in the large pile of colorful cards. How many points are they worth in total?



file_path = "Day 4/text_file.txt"
total_count= 0

with open(file_path, 'r') as file:
    """Read the contents of the file"""
    file_contents = file.read()
    words= file_contents.splitlines()


def total_amount(pick_list):
    list_length= len(pick_list)
    if list_length== 0:
        return 0
    else:
        return 2**(list_length-1)
        

for word in words:
    winning_pick_list= []
    user_pick_list= []
    """Start for loop to parse through text."""
    game_name_split, ticket_number_split=word.split(": ")            # Splits the Game # from the rest of the sentence
    full_card_split=ticket_number_split.split("|")                   # Splits the winning numbers from the user picked numbers
    winning_numbers= full_card_split[0]                              # Creates winning number variable
    user_pick= full_card_split[1]                                    # Creates user pick number variable
    no_spaces_user= user_pick.split(" ")                             # Splits each user item after a space
    no_spaces_winning= winning_numbers.split(" ")                    # Splits each winning item after a space
    
    for number in no_spaces_winning:
        """Deletes empty strings."""
        if number != '':
            winning_pick_list.append(number)
            
    for number in no_spaces_user:
        """Deletes empty strings."""
        if number in winning_pick_list and number != '':
            user_pick_list.append(number)
    
    current_count = total_amount(user_pick_list)
    total_count += current_count

print(f"The total points for the scratchcards are: {total_count}")
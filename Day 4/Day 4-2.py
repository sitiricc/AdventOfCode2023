# --- Part Two ---
# Just as you're about to report your findings to the Elf, one of you realizes that the rules have actually been printed on the back of every card this whole time.

# There's no such thing as "points". Instead, scratchcards only cause you to win more scratchcards equal to the number of winning numbers you have.

# Specifically, you win copies of the scratchcards below the winning card equal to the number of matches. So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

# Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to win any more cards. (Cards will never make you copy a card past the end of the table.)

# This time, the above example goes differently:

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
# Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
# Your copy of card 2 also wins one copy each of cards 3 and 4.
# Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
# Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
# Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
# Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
# Once all of the originals and copies have been processed, you end up with 1 instance of card 1, 2 instances of card 2, 4 instances of card 3, 8 instances of card 4, 14 instances of card 5, and 1 instance of card 6. In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

# Process all of the original and copied scratchcards until no more scratchcards are won. Including the original set of scratchcards, how many total scratchcards do you end up with?

file_path = "Day 4/text_file.txt"
total_count= 0
count= 0
count_dictionary= {}


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

def count_numbers(numbers, user_pick_list):
    number_list = []
    for number in numbers:
        """If the number is not empty and the number is in the user pick list, increment the count."""
        if number != '' and number in user_pick_list:
            number_list.append(number)
    return len(number_list)

def count_numbers(left_numbers, right_numbers):
    matching_numbers = set(left_numbers) & set(right_numbers)
    return len(matching_numbers)



for word in words:
    winning_pick_list= []
    user_pick_list= []
    
    """Start for loop to parse through text."""
    game_name_split, ticket_number_split=word.split(": ")            # Splits the Game # from the rest of the sentence
    game_id = int(game_name_split.split()[1])                        # sprint game index from word Game
    
    full_card_split=ticket_number_split.split("|")                   # Splits the winning numbers from the user picked numbers
    winning_numbers= full_card_split[0]                              # Creates winning number variable
    user_pick= full_card_split[1]                                    # Creates user pick number variable
    no_spaces_user= user_pick.split(" ")                             # Splits each user item after a space
    no_spaces_winning= winning_numbers.split(" ")                    # Splits each winning item after a space
    
    
    for number in no_spaces_winning:
        """Adds number to winning pick list unless they string is empty."""
        if number != '':
            winning_pick_list.append(number)
    
        
    for number in no_spaces_user:
        """If the number is not empty and the number is in the winning pick list, add it to user pick list."""
        if number != '' and number in winning_pick_list:
            user_pick_list.append(number)
    count_dictionary[0]= 1        
    card_numbers = count_numbers(winning_pick_list, user_pick_list)

    
    for number in count_dictionary:
        count_dictionary[game_id] +=1
    
    


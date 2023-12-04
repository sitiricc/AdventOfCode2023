# Our calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.


count= 0
file_path = "Day 1/text_file.txt"
numbers_dictionary = {
    '0': 0,
    '1': 1, 
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def find_match(word, dictionary):
    matches= []
    for i in range (len(word)):
        for j in range (i+1, len(word) +1):
            substring= word[i:j]
            if substring in dictionary:
                matches.append(substring)
    return matches

with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()
    words= file_contents.split()
    
    
    new_digit=0
    first_digit= "0"
    second_digit= "0"
    integer_total= 0
    
    for word in words:
        # print(word) # prints each word
        matching_words= find_match(word, numbers_dictionary)
        
        for letter in matching_words:
            if letter in numbers_dictionary:
                first_digit= str(numbers_dictionary[letter])
                print(first_digit)
                break
        for letter in matching_words[::-1]:
            if letter in numbers_dictionary:
                second_digit= str(numbers_dictionary[letter])
                print(second_digit)
                break
        new_digit= first_digit+second_digit
        integer_total= int(new_digit)
        count += integer_total
        
    print(count)
            
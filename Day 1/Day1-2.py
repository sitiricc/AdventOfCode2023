# Day 1

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.


# Consider your entire calibration document. What is the sum of all of the calibration values?

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

with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()
    words= file_contents.split()
    
    letter_count= 0
    new_digit=0
    first_digit= "0"
    second_digit= "0"
    
    for word in words:
        # print(word) # prints each word
        for letter in word:
            if letter in numbers_dictionary:
                first_digit= str(numbers_dictionary[letter])
                break
        for letter in word[::-1]:
            if letter in numbers_dictionary:
                second_digit= str(numbers_dictionary[letter])
                break
        new_digit= first_digit+second_digit
        integer_total= int(new_digit)
        count += integer_total
        
    print(count)
            
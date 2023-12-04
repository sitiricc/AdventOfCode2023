# Day 1

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?4

count= 0
file_path = "Day 1/text_file.txt"
numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()
    words= file_contents.split()
    
    letter_count= 0
    new_digit=0
    for word in words:
        # print(word) # prints each word
        for letter in word:
            if letter in numbers:
                first_digit= str(letter)
                break
        for letter in word[::-1]:
            if letter in numbers:
                second_digit= str(letter)
                break
        new_digit= first_digit+second_digit
        integer_total= int(new_digit)
        count += integer_total
        
    print(count)
            
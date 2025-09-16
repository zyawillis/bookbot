################################
#   Developed by Zya Willis    #
#         @ BOOKBOT @          #
################################

"""

Bookbot is designed to count the number of words in a ".txt" file - project was given by boot.dev. 
I'd like to expand on this by creating an "average read time" statistic based on how long the average person takes to read X ammount of words

"""

def main():
    
# Define variables

    file_path = "/home/zya/projects/boot.dev/bookbot/books/frankenstein.txt"

# This is the main function of the bookbot 'main.py'
    
    get_book_text(file_path)

    prnt_file_contents = get_book_text(file_path)

### Print whole book to terminal ###

    # print(prnt_file_contents)

    prnt_num_words = num_words(prnt_file_contents)

### Print each word to terminal ###

    print(prnt_num_words)

# Define functions

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

# Import num_words function from "stats.py"
from stats import num_words

main()
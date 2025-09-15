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

# Return the number of words in a string

def num_words(prnt_file_contents):
    """ May need to take out the f statement and tac on later. Need to count the words before output to console """
    split_words = f"{prnt_file_contents.split(" ")} words found in the document"
    return split_words

main()
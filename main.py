def main():
    
# Define variables

    file_path = "/home/zya/projects/boot.dev/bookbot/books/frankenstein.txt"
    word = ""

# This is the main function of the bookbot 'main.py'
    
    get_book_text(file_path)

    prnt_file_contents = get_book_text(file_path)

    print(prnt_file_contents)

# Define functions

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

# Return the number of words in a string

def num_words(file_path):
    
main()
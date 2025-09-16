# Return the number of words in a string

def num_words(prnt_file_contents):
    split_words = prnt_file_contents.split()
    word_len = len(split_words)
    announce = f"{word_len} words found in the document"
    return announce

# Number of times a character appeared.

def character_appearance_count(prnt_file_contents):
    space_char = prnt_file_contents.lower(" ")
    comma_char = prnt_file_contents.lower(",")
    
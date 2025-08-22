def main():
    """
    This is the main function of the bookbot 'main.py'
    """
    file_path = "/home/zya/projects/boot.dev/bookbot/books/frankenstein.txt"
    get_book_text(file_path)
    prnt_file_contents = get_book_text(file_path)
    print(prnt_file_contents)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

main()
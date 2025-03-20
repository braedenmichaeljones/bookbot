from stats import get_word_count
from stats import get_character_count
from stats import sorted_dict_list
import sys

# returns the contents of the book as a string
def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    for i in sys.argv:
        if len(sys.argv) == 1:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            bookpath = sys.argv[1]
    book_text = get_book_text(bookpath)
    num_words = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_dictionary = sorted_dict_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dictionary:
        if item["key"].isalpha():
            print(f'{item["key"]}: {item["value"]}')
    print("============= END ===============")

main()
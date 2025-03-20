# returns number of words in file_contents string
def get_word_count(book_string):
    sep_list = []
    sep_list = book_string.split()
    return len(sep_list)

# takes a string of characters and returns a dictionary counting each character
def get_character_count(book_string):
    book_string = book_string.lower()
    character_dict = {}
    for char in book_string:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sorted_dict_list(character_dict):
    dict_list = [{"key": k, "value": v} for k, v in character_dict.items()]
    dict_list.sort(key=lambda x: x["value"], reverse=True)
    return dict_list
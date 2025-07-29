from stats import get_word_count
from stats import get_num_chars
from stats import get_sort_dicts
import sys


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
    return book_contents


def get_print_format(dict_list):
    for key in dict_list:
        print(f"{key["char"]}: {key["num"]}")
        # print_dict[key["char"]] = key["num"]


def main():
    arg = sys.argv
    if len(arg) == 2:
        book_text = get_book_text(arg[1])
        char_count = get_num_chars(book_text)
        dict_list = get_sort_dicts(char_count)
        word_count = get_word_count(book_text)
        print(
            f"============ BOOKBOT ============ \n Analyzing book found at {arg[1]}... \n ----------- Word Count ---------- \n Found {word_count} total words \n --------- Character Count ---------")
        get_print_format(dict_list)
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()

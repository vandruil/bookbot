from stats import get_word_count
from stats import get_num_chars
from stats import get_sort_dicts


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
    return book_contents


def main():
    input = "books/frankenstein.txt"
    book_text = get_book_text(input)
    char_count = get_num_chars(book_text)
    dict_list = get_sort_dicts(char_count)
    word_count = get_word_count(book_text)
    print(
        f"============ BOOKBOT ============ \n Analyzing book found at {input}... ----------- Word Count ---------- \n Found {word_count} total words \n --------- Character Count --------- \n {dict_list}")


main()

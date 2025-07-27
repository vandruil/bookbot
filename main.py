from stats import get_word_count
from stats import get_num_chars

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_contents = f.read()
    return book_contents






def main():

    book_text = get_book_text("books/frankenstein.txt")
    char_count = get_num_chars(book_text)   
    """word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")
   """
    print(char_count)
main()
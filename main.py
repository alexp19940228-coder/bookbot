from stats import number_of_words
from stats import count_char

def main():
    the_book = "./books/frankenstein.txt"
    text = get_book_text(the_book)
    num_words = number_of_words(text)
    print(f"Found {num_words} total words")
    char_count = count_char(text)
    print(char_count)


def get_book_text(book):
    with open(book) as f:
        return f.read()


main()
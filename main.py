from stats import number_of_words


def main():
    the_book = "./books/frankenstein.txt"
    text = get_book_text(the_book)
    num_words = number_of_words(text)
    print(f"Found {num_words} total words")

def get_book_text(book):
    with open(book) as f:
        return f.read()


main()
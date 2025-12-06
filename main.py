from stats import  result 
from stats import number_of_words
from stats import count_char

def main():
    the_book = "./books/frankenstein.txt"
    text = get_book_text(the_book)

    char_count = count_char(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    print(result(char_count))
    print("============= END ===============")


def get_book_text(book):
    with open(book) as f:
        return f.read()


main()

from stats import get_num_words, number_of_char, sorted_letters
import sys

def get_book_text(path_to_file):
    with open(path_to_file, encoding ='utf-8') as book:
        return book.read()

def main(path):
    book_path = path
    book_content = get_book_text(book_path)
    num_words = get_num_words(book_content)
    num_char = number_of_char(book_content)
    letter_sorted = sorted_letters(num_char)
    
    print(f'============ BOOKBOT ============\nAnalyzing book found at {book_path}\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------')
    for dict in letter_sorted:
        if not dict['char'].isalpha():
            continue
        print(f'{dict["char"]}: {dict["num"]}')
    print('============= END ===============')

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:  
    book_path = sys.argv[1]
    main(book_path)


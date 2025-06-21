def get_num_words(book_content):
    individual_word = book_content.split()
    return len(individual_word)

def number_of_char(book_content):
    content = book_content.lower()
    counter = {}

    for letter in content:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1
    return counter

def sort_on(items):
    return items['num']

def sorted_letters(letter_dict):
    sorted_list = []
   
    for letter in letter_dict:
        sorted_list.append({'char': letter, 'num': letter_dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
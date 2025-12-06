def number_of_words(text):
    text_list = text.split()
    return len(text_list)

def count_char(text):
    dict_char = {}
    for char in text.lower():
        if char not in dict_char:
            dict_char[char] = 1
        else:
            dict_char[char] += 1
    return dict_char
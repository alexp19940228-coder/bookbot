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

# This function needs refactoring.
def result(dict):
    char_list = [{"char": char, "num": count} for char, count in dict.items()]

    def get_num(dictionary):
        return dictionary["num"]

    char_list.sort(key=get_num, reverse = True)
    

    return char_list



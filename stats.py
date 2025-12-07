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

def help_num(text):
    return text["num"]

#takes a dict and return a sorted list
#in the sorted list there is two dicts. each dict should have two key-value pairs, e.g {"char": "a", "num": 5}
#use .sort() to sort from greatest to least

def result(num_char_dict):
    sorted_list = []
    for d in num_char_dict:
        if d.isalpha() == True:
            entry = {
                "char": d,
                "num": num_char_dict[d]
            }
            sorted_list.append(entry)
    sorted_list.sort(key=help_num, reverse=True)
    return sorted_list


    




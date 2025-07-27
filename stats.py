def get_word_count(book_text):
    list_string = book_text.split()
    return len(list_string)

def get_num_chars(book_text):
    list_string = book_text.lower()
    dic_chars = {}
    for char in list_string:
        if char not in dic_chars:
            dic_chars[char] = 1
        else:
            dic_chars[char] += 1
    return dic_chars

def get_sort_dicts(dict):
    dic_list = []
    for key in dict:
        if key.isalpha():
            new_dict = {"char": key,
                    "num": dict[key]
                      }
            dic_list.append(new_dict)
    dic_list.sort(key=lambda x: x["num"],reverse=True)
    return dic_list
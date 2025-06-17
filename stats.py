


def num_words(text: str) -> int:
    return len(text.split())

def count_chars(text: str)-> dict:
    chars = {}
    text = text.lower()
    for char in text:
        if char not in chars:
            chars[char] = 1
        elif char in chars:
            chars[char] +=1
    return chars

def report(char_count:dict)-> list: 
    char_list = []
    for k,v in char_count.items():
        dummy_dict = {"char": k, "num": v}
        char_list.append(dummy_dict)
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list





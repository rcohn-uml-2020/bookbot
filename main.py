def main():
    book_path = "books/frankenstein.txt"
    text = read(book_path)
    char_dict = assign_characters(text)
    
    print("Report for: " + book_path)

    print("~~~")

    print(f"There are {parser(text)} characters in total")

    print("~~~")

    for key in char_dict.keys():
        print(f"Character '{key}' was found {char_dict[key]} times")
    
    print("")

    print("~End~")

def read(path):
    with open(path) as f:
        return f.read()

def parser(file):
    return len(file.split())

def assign_characters(file):
    lowered = file.lower()
    char_list = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    for c in lowered:
        if c in char_list:
            char_list[c] += 1
    return char_list


main()

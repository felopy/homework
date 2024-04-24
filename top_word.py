"Word Frequency Counter"

def return_file(fname):
    "return file"
    try:
        with open(fname,"r",encoding = "utf-8") as file:
            return file.read()
    except  FileNotFoundError:
        print("FileNotFoundError")
    return None

def create_a_frequency_library(file):
    "creates a library in which words are written according to their frequency"
    word_dict = {}
    for i in file:
        if not i.isalpha() and i != " ":
            file = file.replace(i,"").lower()
    file_split = file.split()
    for i in file_split:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    return word_dict

def sort_dict(dict_word):
    "sorts the library in ascending order and returns the last element"
    list_dict = list(dict_word.items())
    list_dict.sort(key = lambda x: x[1])
    return list_dict[-1]

def main():
    "execute code"
    file_read = return_file("text.txt")
    word_dict = create_a_frequency_library(file_read)
    print(sort_dict(word_dict))
if __name__ =="__main__":
    main()

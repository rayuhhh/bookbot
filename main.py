from stats import num_words, count_chars, report
import sys


#frankenstein = "books/frankenstein.txt"
# removed hard coded book path for a command line argument
def get_book_text(file_path: str)-> str:
    with open(file_path) as f:
        #file_contents = f.read()
        return f.read()



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    text = get_book_text(sys.argv[1]) # open book func, return string of book's content
    number_of_words = num_words(text) # number of words in string
    #print(f"{number_of_words} words found in the document")
    char_dict = count_chars(text)
    
    list_of_chardict = report(char_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for d in list_of_chardict:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")        



if __name__ == "__main__":
    main()
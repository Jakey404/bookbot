import sys

from stats import get_num_words, get_num_chars, sort_char

def get_book_text(filepath):
    with open(filepath, "r") as f:
        contents = f.read() 
    return contents

def count_words(text):
    words = text.split()
    return len(words)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
   
    num_words = get_num_words(text)
    char_counts = get_num_chars(text)
    sorted_chars = sort_char(char_counts)
   
   # Print the report
    print("========= BOOKBOT =========")
    print(f"Analyzing book found at {filepath}...")
    print("--------- Word Count ---------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for item in sorted_chars:
       print(f"{item['char']}: {item['num']}")
    print("========= END =========")

main()
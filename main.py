import sys
from stats import get_num_words, get_char_count, make_sorted_list

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    # 1) Require exactly one argument: the path to the book
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    # 2) Read and analyze
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_counts = make_sorted_list(char_count)

    # 3) EXACT required output strings
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_counts:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")

if __name__ == "__main__":
    main()


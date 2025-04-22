from stats import word_number, char_count, sort_char_count
import sys

def get_book_text(location):
    with open(location) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        location = sys.argv[1]
        book_text = get_book_text(location)
        words = word_number(book_text)
        chars = char_count(book_text)
        sorted_char = sort_char_count(chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {location}...")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        for char, count in chars.items():
            print(f"{char}: {count}")
        print("============= END ===============")


main()


import sys
from stats import get_num_words, get_character_counts


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_file = sys.argv[1]
    try:
        file_contents = read_file(book_file)
        word_count = get_num_words(file_contents)
        character_counts = get_character_counts(file_contents)
        print_report(book_file, word_count, character_counts)
    except FileNotFoundError:
        error_message = (
            f"Error: File {book_file} not found. "
            "Please check that it exists."
        )
        print(error_message)
    except PermissionError:
        error_message = (
            f"Error: File {book_file} is not accessible. "
            "Please check that you have permission to read it."
        )
        print(error_message)


def read_file(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        return file_contents


def print_report(file_name, word_count, character_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character_count in character_counts:
        character = character_count["character"]
        count = character_count["count"]
        print(f"{character}: {count}")
    print("============= END ===============")


main()

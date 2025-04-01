from stats import get_num_words, get_character_counts

def main():
    book_file = "books/frankenstein.txt"
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
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document")
    print()
    for character_count in character_counts:
        character = character_count["character"]
        count = character_count["count"]
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")


main()

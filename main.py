def main():
    book_file = "books/frankenstein.txt"
    try:
        file_contents = read_file(book_file)
        word_count = count_words(file_contents)
        character_counts = count_alphabet_characters(file_contents)
        sorted_character_counts = sort_character_counts(character_counts)
        print_report(book_file, word_count, sorted_character_counts)
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


def count_words(text):
    return len(text.split())


def count_alphabet_characters(text):
    characters = {}
    for character in text.lower():
        if character.isalpha():
            characters[character] = characters.get(character, 0) + 1
    return characters


def sort_character_counts(character_counts):
    character_count_list = []
    for character, count in character_counts.items():
        character_count_list.append({"character": character, "count": count})
    character_count_list.sort(key=sort_on_count, reverse=True)
    return character_count_list


def sort_on_count(character_count):
    return character_count["count"]


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

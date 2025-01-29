def main():
    book_file = "books/frankenstein.txt"
    with open(book_file) as f:
        file_contents = f.read()

        word_count = count_words(file_contents)
        character_count = count_alphabet_characters(file_contents)

        print_report(book_file, word_count, character_count)


def count_words(text):
    return len(text.split())


def count_alphabet_characters(text):
    characters = {}
    for character in text.lower():
        if character.isalpha():
            characters[character] = characters.get(character, 0) + 1
    return sorted(characters.items(), key=lambda x: x[1], reverse=True)


def print_report(file_name, word_count, character_count):
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document")
    print()
    for character, count in character_count:
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")


main()

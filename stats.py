def get_num_words(text):
    return len(text.split())


def get_character_counts(text):
    character_counts = count_alphabet_characters(text)
    return sort_character_counts(character_counts)


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
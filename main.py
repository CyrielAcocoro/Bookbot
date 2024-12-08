def main():

    with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    book_path = "books/frankenstein.txt"
    def count_string(text_string):
        return len(text_string.split())
    words_in_docs = count_string(file_contents)

    def character_appearance(text_in_book):
        characters_dict = {}
        lowered_text = text_in_book.lower()
        for char in lowered_text:
            if char.isalpha(): 
                if char in characters_dict:
                    characters_dict[char] += 1
                else:
                    characters_dict[char] = 1
        return characters_dict
    character_dictionary = character_appearance(file_contents)

    def print_report(dict, number_words):
        print(f"--- Begin report of {book_path} ---")
        print(f"{number_words} words found in the document")
        print()
        for key,value in dict.items():
            print(f"The {key} character was found {value} times")
        print("--- End report ---")
    print_report(character_dictionary, words_in_docs)
main()
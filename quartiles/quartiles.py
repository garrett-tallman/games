from itertools import permutations

def find_valid_words(tiles, dictionary_path):
    # Use a set for faster lookups
    try:
        with open(dictionary_path) as f:
            dictionary = set(word.strip().upper() for word in f)
    except FileNotFoundError:
        print(f"Dictionary file not found at {dictionary_path}")
        return

    answers = []
    # Generate all combinations of 4 tiles
    for i in range(2, 5):
        quartiles = permutations(tiles, i)
        for q in quartiles:
            word = "".join(q)
            if word.upper() in dictionary:
                answers.append(word)

    return answers

def main():
    tiles = [
        "mob", "ker", "wo", "ate", "er", "dem", "an", "ize", "wor", "od",
        "on", "il", "and", "is", "sl", "ms", "str", "org", "ous", "im"
    ]
    dictionary_path = "sowpods.txt"

    valid_words = find_valid_words(tiles, dictionary_path)
    if valid_words:
        print("Found valid words:")
        for word in valid_words:
            print(word)
    else:
        print("No valid words found.")

if __name__ == "__main__":
    main()

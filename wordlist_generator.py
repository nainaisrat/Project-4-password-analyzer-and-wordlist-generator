import itertools

def generate_variants(words):
    patterns = []
    for word in words:
        variants = [
            word,
            word.capitalize(),
            word + "123",
            word[::-1],
            word.replace('a', '@').replace('e', '3'),
        ]
        patterns.extend(variants)
    return patterns

def save_wordlist(words, filename="wordlist.txt"):
    with open(filename, "w") as f:
        for word in words:
            f.write(f"{word}\n")

if __name__ == "__main__":
    inputs = input("Enter personal info (comma separated: name, birth year, pet): ")
    base_words = [item.strip() for item in inputs.split(",")]
    wordlist = generate_variants(base_words)
    save_wordlist(wordlist)
    print(f"Wordlist saved to wordlist.txt with {len(wordlist)} entries.")

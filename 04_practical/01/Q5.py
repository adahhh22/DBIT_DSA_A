text = "data structures and algorithms"
char_freq = {}

for char in text:
    if char != ' ':
        char_freq[char] = char_freq.get(char, 0) + 1

for char, count in char_freq.items():
    print(f"'{char}': {count}")
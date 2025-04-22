def word_number(text):
    words = text.split()
    word_count = len(words)
    return word_count

def char_count(text):
    words = text.split()
    char_count = {}

    for word in words:
        for char in word:
            if char.isalpha():
                char = char.lower()
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

    return char_count


def sort_char_count(char_count):
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_char_count
"""
Input a string.
Example:
Input: can you can a can as a canner can can a can
Output: can
"""

def count(text):
    """Return the most frequently used word in a text."""
    word_count = dict()
    words = text.split()
    max_c = 0
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

        if word_count[word] > max_c:
            max_c = word_count[word]
            popular_word = word
        elif word_count[word] == max_c:
            popular_word = '-'

    return popular_word

TEXT = input()
print(count(TEXT))


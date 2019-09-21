def count(text):
    word_count = dict()
    words = text.split()
    max_c = 0
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

        if (word_count[word] > max_c):
            max_c = word_count[word]
            popular_word = word
        elif (word_count[word] == max_c):
            popular_word = '-'

    return popular_word

print(count(input()))


def duplicate_encode(word):
    new_word = ''
    for letter in word:
        word = word.lower()
        letter = letter.lower()
        if word.count(letter) > 1:
            new_word += ')'
        else:
            new_word += '('
    return new_word


print(duplicate_encode('recede'))
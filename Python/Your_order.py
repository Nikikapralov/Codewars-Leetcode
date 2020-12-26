def order(sentence):
    data = sentence.split()
    list_sentence = ["" for item in range(len(data))]
    for word in data:
        for symbol in word:
            if symbol.isdigit():
                symbol = int(symbol)
                list_sentence[symbol - 1] = word
    result = ' '.join(list_sentence)
    return result

print(order("is2 Thi1s T4est 3a"))


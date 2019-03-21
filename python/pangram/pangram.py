def is_pangram(sentence):
    sentence_lower = sentence.lower()
    alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    alphabet_len = len(alphabet_string)
    for letter in alphabet_string:
        if letter in sentence_lower:
            count += 1
    if count == alphabet_len:
        return True
    else:
        return False

def sort_sentence(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    sorted_words = sorted(words, key=lambda x: int(''.join(filter(str.isdigit, x))))
    return ' '.join(sorted_words)


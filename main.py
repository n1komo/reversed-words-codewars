def reverse_words(s):
    splitted = s.split(' ')
    splitted.reverse()
    reversed_str = ' '.join(splitted)
    return reversed_str

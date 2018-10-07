from collections import Counter
import string


def calc_word_cloud(line: str) -> Counter:
    table = dict.fromkeys([p for p in string.punctuation], "")
    line = line.translate(str.maketrans(table)).lower()
    words = line.split(" ")
    return Counter(words)

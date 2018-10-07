from collections import Counter
import string


def calc_word_cloud_n(line: str) -> Counter:
    count = Counter()
    word = ""

    def inc_word_count():
        nonlocal word
        count[word] += 1
        word = ""

    for c in line:
        if c not in string.punctuation and c != " ":
            word += c.lower()
        elif c == "'":
            continue
        elif c in string.punctuation and len(word) > 0:
            inc_word_count()
        elif c == " " and len(word) > 0:
            inc_word_count()

    if len(word) > 0:
        inc_word_count()

    return count

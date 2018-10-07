def is_any_permutation_palindrome(word: str) -> bool:
    """
    Given an input word, return true if any permuatation of the chars in the
    word is a palindrome. Else, return false.
    """
    chars = set()

    for char in list(word):
        if char in chars:
            chars.remove(char)
        else:
            chars.add(char)

    return len(chars) <= 1

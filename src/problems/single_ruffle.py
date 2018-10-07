def is_single_ruffle(shuffled_deck, half1, half2):
    """
    Takes the shuffled deck and the two halves and returns true if the
    shuffled deck is a single ruffle of the two halves. Else, it returns
    false.
    """
    half1_index = 0
    half2_index = 0
    shuffled_deck_index = 0

    while shuffled_deck_index < len(shuffled_deck):
        if half1_index < len(half1) and half1[half1_index] == shuffled_deck[shuffled_deck_index]:
            half1_index += 1
        elif half2_index < len(half2) and half2[half2_index] == shuffled_deck[shuffled_deck_index]:
            half2_index += 1
        else:
            return False

        shuffled_deck_index += 1

    return True

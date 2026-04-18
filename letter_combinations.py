DIGITS_TO_LETTERS = {
    '2': 'abc', 
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

def letter_combinations(digits: str) -> list[str]:
    """ All possible letter combinations for a given strings of digits
    args: digits: a string of digits from 2-9; empty strig also valid
    
    returns: a list of all possible letter combinations that the number could represnt
    """
    if not digits or len(digits) > 4:
        return []
    combinations = ['']


    for digit in digits:
        digit_letters = DIGITS_TO_LETTERS.get(digit, '')
        new_combinations = []
        for combo in combinations:
            for letter in digit_letters:
                new_combinations.append(combo + letter)
        combinations = new_combinations
    return combinations if combinations != [''] else []
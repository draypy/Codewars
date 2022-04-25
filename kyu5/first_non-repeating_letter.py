"""
https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python
"""


def first_non_repeating_letter(string):
    data = {}
    for symbol in string:
        data[symbol.lower()] = data.get(symbol.lower(), 0) + 1
    for symbol in string:
        if data[symbol.lower()] == 1:
            return symbol
    return ''

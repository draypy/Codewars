"""
https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
"""


def spin_words(sentence):
    data = sentence.split()
    for _index in range(len(data)):
        if len(data[_index]) > 4:
            data[_index] = data[_index][::-1]
    return ' '.join(data)

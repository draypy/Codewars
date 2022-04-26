"""
https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
"""


def generate_hashtag(s):
    if 0 < len(s) < 140:
        return '#' + s.title().replace(' ', '')
    return False

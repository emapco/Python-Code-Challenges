import re

# determines if a given string is a palindrome
# case-insensitive and non-alpha character insensitive
def is_palindrome(string: str) -> bool:
    is_palindrome_str = True
    # join characters that are alpha while ignoring case
    modified_str = ''.join(filter(str.isalpha, string.upper()))
    # iterate through string and compare each character in the string
    # to its complementary character
    str_length = len(modified_str)
    for i in range(str_length // 2):
        if i > str_length - i:
            break
        elif modified_str[i] != modified_str[(str_length - 1) - i]:
            is_palindrome_str = False
    return is_palindrome_str


def solution(string):
    # join characters using regex while ignoring case
    forwards = ''.join(re.findall(r'[a-z]+', string.lower()))
    # create a copy of forwards with stride = -1
    # thus reversing the string
    backwards = forwards[::-1]
    # return boolean equality comparison of the strings
    return forwards == backwards

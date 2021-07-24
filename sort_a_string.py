# function that sorts the words in a string
# ignores case when sorting but outputs the original cases for each word
def sort_words(string: str) -> str:
    split_str = string.split()
    str_length = len(split_str)
    for i in range(str_length):
        for j in range(1, str_length):
            if split_str[i].lower() < split_str[j].lower():
                temp = split_str[i]
                split_str[i] = split_str[j]
                split_str[j] = temp
    return " ".join(split_str)


def solution(input_str):
    # get list of words separated by ' '
    words = input_str.split()
    # append lowercase copy of word to the front of each word
    words = [w.lower() + w for w in words]
    # call python built-in sort method for strings
    words.sort()
    # list comprehension that keeps the second half of the (original) word
    words = [w[len(w)//2] for w in words]
    return ' '.join(words)

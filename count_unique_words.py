from collections import Counter
import re
import string


# counts the number of unique words and how often each occurs
def count_unique_words(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        # regex matches all characters that are not alphanumeric, ', or -
        forbidden_characters = ''.join([re.match("[^0-9a-zA-Z'-]+", char).string
                                        for char in string.printable
                                        if re.match("[^0-9a-zA-Z'-]+", char)])

        word_counts = Counter()
        for lines in file.readlines():
            for word in lines.lower().split():
                word_counts[word.strip(forbidden_characters)] += 1

        total = sum(word_counts[key] for key in word_counts.keys())
        print(f"Total Words: {total}\n")
        print("Top 20 Words:")
        for item in word_counts.most_common(20):
            print("{:<20} {}".format(item[0], item[1]))
    return word_counts


# does not properly parse "ALL'S"
def solution(path):
    with open(path, encoding='utf8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print("\nTotal Words:", len(all_words))

        word_counts = Counter()
        for word in all_words:
            word_counts[word] += 1

        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(word[0], '\t', word[1])
    return word_counts

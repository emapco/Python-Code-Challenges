from secrets import choice


# generate a password using diceware list to randomly
# generate phrases from random ints
def generate_diceware_password(num_words):
    diceware_num_digits = 5
    with open('additional-files/diceware_list.txt', 'r') as file:
        diceware_dictionary = {line.split()[0]: line.split()[1] for line in file.readlines()}
        # list of joined lists; each joined list represents a diceware number
        diceware_numbers = ["".join([str(choice(range(1, 6))) for _ in range(diceware_num_digits)])
                            for _ in range(num_words)]
        pass_phrase = [diceware_dictionary[number] for number in diceware_numbers]
        return ' '.join(pass_phrase)


def solution(num_words):
    with open('additional-files/diceware_list.txt', 'r') as file:
        lines = file.readlines()
        word_list = [line.split()[1] for line in lines]

    words = [choice(word_list) for i in range(num_words)]
    print(words)
    return ' '.join(words)

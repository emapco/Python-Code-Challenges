import pickle

# saves/pickles a dictionary to a .dat binary file
def save_dictionary(dictionary, output_file_path):
    output_file = open(output_file_path, 'wb')
    pickle.dump(dictionary, output_file)
    output_file.close()

# loads/unpickles a dictionary from a .dat binary file
def load_dictionary(input_file_path):
    input_file = open(input_file_path, 'rb')
    dictionary = pickle.load(input_file)
    input_file.close()
    return dictionary

def solution_save(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)

def solution_load(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

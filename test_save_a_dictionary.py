from unittest import TestCase


class Test_save_dictionary(TestCase):
    def test_save_dictionary(self):
        dictionary = {'a': 7, 'b': 5, 'c': 1}
        file_path = 'dict.dat'
        from save_a_dictionary import save_dictionary
        self.assertIsNone(save_dictionary(dictionary, file_path))


class Test_sort_dictionary(TestCase):
    def test_sort_dictionary(self):
        answer = {'a': 7, 'b': 5, 'c': 1}
        file_path = 'dict.dat'
        from save_a_dictionary import load_dictionary
        self.assertEqual(load_dictionary(file_path), answer)

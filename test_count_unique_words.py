from unittest import TestCase

class Test_count_unique_words(TestCase):
    def test_count_unique_words_short(self):
        from count_unique_words import count_unique_words, solution
        self.assertEqual(count_unique_words('additional-files/input_string.txt')['the'], 3)

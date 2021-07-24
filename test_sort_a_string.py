from unittest import TestCase

# auto-test toggled test class to monitor changes to sort_words function
class Test_sort_words(TestCase):
    def test_sort_words(self):
        from sort_a_string import sort_words
        self.assertEqual(sort_words("string of words"), "of string words")

    def test_sort_words_with_uppercase(self):
        from sort_a_string import sort_words
        self.assertEqual(sort_words("banana ORANGE apple"), "apple banana ORANGE")

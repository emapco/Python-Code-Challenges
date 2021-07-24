from unittest import TestCase

# auto-test toggled test class to monitor changes to is_palindrome function
class Test_is_palindrome(TestCase):
    def test_is_palindrome(self):
        from identify_a_palindrome import is_palindrome
        self.assertTrue(is_palindrome("Asdfdsa"))
        self.assertTrue(is_palindrome("asDf'ssfdsa"))

    def test_is_palindrome_with_non_alpha(self):
        from identify_a_palindrome import is_palindrome
        self.assertTrue(is_palindrome("asdf'ssfdsa"))

    def test_is_not_palindrome(self):
        from identify_a_palindrome import is_palindrome
        self.assertFalse(is_palindrome("asdfddsa"))
        self.assertFalse(is_palindrome("hello world"))

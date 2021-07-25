from unittest import TestCase


class Test_generate_diceware_password(TestCase):
    def test_generate_diceware_password(self):
        from generate_a_password import generate_diceware_password
        pass_phase_words = 5
        # check if password contains the specified amount of words
        self.assertEqual(len(generate_diceware_password(pass_phase_words).split()), pass_phase_words)

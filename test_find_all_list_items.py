from unittest import TestCase


class Test_index_all(TestCase):
    def test_index_all(self):
        example = [1, 2, 3, 3, 5, 3]
        answer = [[2], [3], [5]]
        from find_all_list_items import index_all
        self.assertEqual(index_all(example, 3), answer)

    def test_index_all_nested_list(self):
        example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
        answer = [[0, 0, 1], [0, 1], [1, 1]]
        from find_all_list_items import index_all
        self.assertEqual(index_all(example, 2), answer)

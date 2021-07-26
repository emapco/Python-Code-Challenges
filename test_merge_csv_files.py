from unittest import TestCase


class Test_merge_csv_files(TestCase):
    def test_merge_csv_files(self):
        from merge_csv_files import merge_csv_files
        directory = 'additional-files/'
        input_files = [directory + 'students1.csv', directory + 'students2.csv']
        output_file = directory + 'students.csv'
        solution_file = directory + 'students_solution.csv'
        merge_csv_files(input_files, output_file)
        with open(output_file, 'r') as file, open(solution_file, 'r') as solution:
            self.assertEqual(file.read(), solution.read())

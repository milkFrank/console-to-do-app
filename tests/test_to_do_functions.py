import unittest
from unittest.mock import patch
from logic import to_do_functions as tdf

class ToDoFunctionsTestCase(unittest.TestCase):
    """Tests for some functions in to_do_functions"""

    @patch('builtins.input', side_effect=['123', '-49', '3'])
    def test_task_number(self, mock_input):
        """Should ignore any number that not in the list"""
        fake_menu = ['Task 1', 'Task 2', 'Task 3'] # Create a fake menu to show
        # that function works with any menu given
        task_number = tdf.ask_task_number(fake_menu)
        self.assertEqual(task_number, 3)

    @patch('builtins.input', return_value='0')
    def test_task_number_zero(self, mock_input):
        """Should return 0, because it means «go back» in function"""
        fake_menu = ['Task 1', 'Task 2', 'Task 3'] # Create a fake menu to show
        # that function works with any menu given
        task_number = tdf.ask_task_number(fake_menu)
        self.assertEqual(task_number, 0)

if __name__ == '__main__':
    unittest.main()

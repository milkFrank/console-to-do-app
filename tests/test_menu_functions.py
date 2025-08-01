import unittest
from unittest.mock import patch
from logic import menu_functions as mf
from data import data_structures as ds


class MenuFunctionsTestCase(unittest.TestCase):
    """Tests for some functions in «menu_functions.py»"""

    @patch('builtins.input',
        side_effect=['igjoasoijgf', '321guy', '!!??&^', '', '2'])

    def test_check_valid_number(self, mock_input):
        """Should ignore any string inputs that doesn't convert to int-type"""
        number = mf.check_valid_number()
        self.assertEqual(number, 2)

    @patch('builtins.input', side_effect=['15', '-24', '3'])

    def test_menu_number(self, mock_input):
        """Should ignore any number that not in the menu"""
        fake_menu = {1: "Action1", 2: "Action2", 3: "Action3"} # Create a fake
        # menu to show that function works with any menu given
        menu_option = mf.ask_menu_number(fake_menu)
        self.assertEqual(menu_option, 3)


if __name__ == '__main__':
    unittest.main()

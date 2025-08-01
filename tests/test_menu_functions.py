import unittest
from unittest.mock import patch
from logic import menu_functions as mf
from data import data_structures as ds


class MenuFunctionsTestCase(unittest.TestCase):
    """Tests for some functions in «menu_functions.py»"""

    @patch('builtins.input',
        side_effect=['igjoasoijgf', '321guy', '!!??&^', '', '2'])

    def test_string_input_in_menu(self, mock_input):
        """Should ignore any string inputs that doesn't convert to int-type"""
        menu_option = mf.ask_menu_number(ds.main_menu)
        self.assertEqual(menu_option, 2)


if __name__ == '__main__':
    unittest.main()

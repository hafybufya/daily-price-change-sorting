# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import unittest
from unittest.mock import Mock, MagicMock, patch
from mainCode import *
import pytest
import os

# ---------------------------------------------------------------------
# Class of unit tests
# ---------------------------------------------------------------------
class my_unit_tests(unittest.TestCase):

    # ---------------------------------------------------------------------
    # File handling unit tests
    # ---------------------------------------------------------------------

    # Tests if the csv file has been saved
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile('historicalData.csv'))

    # ---------------------------------------------------------------------
    # TESTING: read_nordic_data()
    # ---------------------------------------------------------------------

    # Tests if the df file has the Daily Price colum made
    def test_df_headings(self):
        if 'Daily Price Change' in df:
            result = True
        self.assertEqual(result, True)



 
    # run the tests
if __name__ == "__main__":
    unittest.main()


# y = 4.07x -0.67
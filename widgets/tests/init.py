import unittest
from test_button import TestButton
from test_dropdown import TestDropdown
from test_input import TestInput
from test_label import TestLabel
from test_progress_bar import TestProgressBar
from test_table import TestTable
from test_text_box import TestTextBox

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestButton())
    suite.addTest(TestDropdown())
    suite.addTest(TestInput())
    suite.addTest(TestLabel())
    suite.addTest(TestProgressBar())
    suite.addTest(TestTable())
    suite.addTest(TestTextBox())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

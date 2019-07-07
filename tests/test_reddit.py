import reddit
import unittest

class TestReddit(unittest.TestCase):
    """
    Test the add function from the mymath library
    """
    def setUp(self):
        self.

    def tearDown(self):
        # self.widget.dispose()
        pass

    def test_get_reddit(self):
        reddit = get_reddit(config)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')


if __name__ == '__main__':
    unittest.main()

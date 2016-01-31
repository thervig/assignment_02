import unittest

class TestAssignmentTwo_None(unittest.TestCase):

    def setUp(self):
        pass

    def test_none_is_universal(self):
        """
        Think about what 'is' does here.
        """
        truth = True
        self.assertEqual(truth, None is None)

    def test_none_is_unique(self):
        """
        This is a great place to launch an interpreter and check
         what the right hand side of the equalities evaluate to.
        """
        truth = 1
        self.assertEqual(truth, None is not True)
        truth = 1 # This resets the value of truth
        self.assertEqual(truth, None is not False)

    def test_none_existence(self):

        x = 1
        checker = None
        if checker:
            x = 1
        self.assertEqual(1,x)

    def test_truthiness(self):
        """
        Compare this test to the above.
        """
        x = []  # An empty list
        y = 0
        if not x:
            y = 1
        self.assertEqual(1, y)

        self.assertFalse(x == 0)  # Not PEP8 compliant, but commonly used.

        """
        The take away here is that truthiness is not the same as None
        None evaluates to False in these if statements, as does an
        empty list, but None != (is not equal to) False.
        """

    def tearDown(self):
        pass


class TestAssignmentTwo_Strings(unittest.TestCase):

    def setUp(self):
        pass

    def test_quotations(self):
        """
        Replace the blanks with a boolean and think about
        why you might want to utilize different quotation
        mechanisms.
        """

        string = 'Hello World'
        self.assertEqual(True, isinstance(string, str))

        string = "Hello World"
        self.assertEqual(True, isinstance(string, str))

        string = '''Hello World'''
        self.assertEqual(True, isinstance(string, str))

        string = """Hello World"""
        self.assertEqual(True, isinstance(string, str))

    def test_escaping_quotes(self):
        """
        Another replacement.  This tests mirrors common
        data munging techniques.  For example if needing
        to modify a string column of a shapefile and maintain
        some quotation scheme.
        """
        a = "He said, \"Don't forget to relax a little\""
        b = 'He said, "Don\'t" forget to relax a little'

        self.assertEqual(False, a == b)

    def test_string_concatenation(self):
        """
        Concatenation is either explicit or implicit.
        See the Zen of Python for which is preferable
        """
        string = "Go" + " Sun Devils"
        self.assertEqual("Go Sun Devils", string)

        string = "Go" " Sun Devils"
        self.assertEqual("Go Sun Devils", string)

    def test_in(self):
        """
        The in operator can be helpful in finding
        substrings.
        Once the complexity gets high, I would suggest switching
        to the 're' module (for Regex).
        For these, fix the assertion methods
        """
        cities = '"New York", "Boston", "Chicago", "Dallas", "St. Louis", "Phoenix" '
        self.assertTrue("Dallas" in cities)
        self.assertTrue('"Dallas"' in cities)
        self.assertTrue('ton' in cities)
        self.assertTrue("\", \"" in cities)

    def test_format(self):
        """
        This is presented in a style that I frequently use
        to debug something simple (when I do not want to
        use a debugger)
        """

        s = 'The current index is {}'
        self.assertEqual(True,isinstance(s, str))

        i = 0

        truth = 'The current index is 0'  # Replace the ____
        self.assertEqual(truth, s.format(i))

    def test_string_cases(self):
        """
        Another common string manipulation set borrowed from
        Python Koans.
        """
        self.assertEqual('Guido', 'guido'.capitalize())
        self.assertEqual('GUIDO', 'guido'.upper())
        self.assertEqual('timbot', 'TimBot'.lower())
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())

    def test_format_rounding(self):
        """
        This test mirrors real world code that I use frequently.
        Assume that you have a bunch of data in a cvs file.  You
        have read in the data and now want to print some of it
        to screen or pipe it into another file.  The only thing is,
        the new output can be much less precise.
        """

        pi = 3.14159265  # Please use math.pi if you ever really need to use pi
        s = '{}'

        # Check to see what the heck 's' is
        self.assertEqual(True, isinstance(s, str))

        rounded_pi = '3.1416'
        self.assertEqual(rounded_pi, s.format(round(pi, 4)))

    def test_translation(self):
        """
        Take a look at the string module to see how this is working.
        The example is from PyMoTW (see the syllabus for a link).
        In Python 3 (the version we are using) `maketrans` has moved
        from the string module to a method on the `str` type.  This
        is why we do not need to `import string`
        Fill in the truth value
        """

        leet = str.maketrans('abegiloprstz', '463611092572')
        s = 'The quick brown fox jumped over the lazy dog.'
        s.translate(leet)  # Translate the string here

        truth = 'The quick brown fox jumped over the lazy dog.'  # Truth is the newly translated string

        self.assertEqual(truth, s)

    def test_write_your_own(self):
        """
        Write your own test here demonstrating either string
        or None usage that has not been demonstrated above.
        """
        x = 2016
        self.assertIsNotNone(True, x)  # You can either fix this line or remove it once the test is in.

    def tearDown(self):
        pass

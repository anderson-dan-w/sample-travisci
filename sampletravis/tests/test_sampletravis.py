import unittest

#import foo
#import sampletravis
from sampletravis import foo

class TestSampleTravis(unittest.TestCase):
    def test_double_int(self):
        num = 4
        expected = 8
        self.assertEqual(expected, foo.double(num))


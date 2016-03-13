import unittest
import sampletravis

class TestSampleTravis(unittest.TestCase):
    def test_double_int(self):
        num = 4
        expected = 8
        self.assertEqual(expected, sampletravis.double(num))


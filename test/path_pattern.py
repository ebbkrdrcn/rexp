import unittest, re
from rexp.patterns import PathPattern

class PathPatternTestMethods(unittest.TestCase):

    def test_path(self):
        callable = PathPattern()
        e1 = callable('/')
        d1 = '/usr/local/lib/'
        m1 = re.match(e1, d1)
        self.assertIsNotNone(m1)
        self.assertEqual(m1.group(0), d1)

        e2 = callable('\\')
        d2 = 'c:\\usr\\local\\lib\\'
        m2 = re.match(e2, d2)
        self.assertIsNotNone(m2)
        self.assertEqual(m2.group(0), d2)

        try:
            callable('|')
        except:
            self.assertIsNotNone(callable('/'))
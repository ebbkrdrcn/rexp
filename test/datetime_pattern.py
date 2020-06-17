import unittest, re
from rexp.patterns import DateTimePattern

class DateTimePatternTestMethods(unittest.TestCase):
    def test_format(self):
        callable = DateTimePattern()
        e1 = callable('%Y')
        e2 = callable('%Y-%m')
        e3 = callable('%Y-%m-%d')
        e4 = callable('T%H')
        e5 = callable('T%H:%M')
        e6 = callable('T%H:%M:%S')
        e7 = callable('%z')

        date = '1994-10-05T08:15:30-05:00'

        m1 = re.search(e1, date)
        self.assertEqual(m1.group(0), '1994')

        m2 = re.search(e2, date)
        self.assertEqual(m2.group(0), '1994-10')

        m3 = re.search(e3, date)
        self.assertEqual(m3.group(0), '1994-10-05')

        m4 = re.search(e4, date)
        a = m4.group(0)
        self.assertEqual(m4.group(0), 'T08')

        m5 = re.search(e5, date)
        self.assertEqual(m5.group(0), 'T08:15')

        m6 = re.search(e6, date)
        self.assertEqual(m6.group(0), 'T08:15:30')

        m7 = re.search(e7, date)
        self.assertEqual(m7.group(0), '-05:00')

        date1 = '1994-11-05T08:15:30-05:00'
        e8 = callable('%Y-%m-%dT%H:%M:%S%z')
        m8 = re.search(e8, date1)
        self.assertEqual(m8.group(0), '1994-11-05T08:15:30-05:00')




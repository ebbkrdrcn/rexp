import unittest, re
from rexp.patterns import UUIDPattern

class UUIDPatternTestMethods(unittest.TestCase):

    def test_format(self):
        callable = UUIDPattern()
        format = r'[0-9a-f]{8}-[0-9a-f]{4}-%s[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}'
        for ver in range(1, 6):
            a = callable.__call__(ver)
            b = format % ver
            self.assertEqual(a, b)

        a = callable()
        b = format % '[1-5]'
        self.assertEqual(a, b)

        try:
            callable(10)
        except ValueError:
            self.assertTrue(1)


    def test_version(self):
        from uuid import uuid1, uuid3, uuid4, uuid5
        callable = UUIDPattern()
        values = [
            'd574b8fa-28dc-11e7-93ae-92361f002671',
            'd574b8fa-28dc-21e7-93ae-92361f002671',
            'd574b8fa-28dc-31e7-93ae-92361f002671',
            'd574b8fa-28dc-41e7-93ae-92361f002671',
            'd574b8fa-28dc-51e7-93ae-92361f002671'
        ]

        for ver in range(0, 10):
            if ver > 0 and ver < 6:
                self.assertIsNotNone(re.match(callable(ver), values[ver - 1]))
            else:
                try:
                    callable(ver)
                except ValueError:
                    self.assertTrue(1)






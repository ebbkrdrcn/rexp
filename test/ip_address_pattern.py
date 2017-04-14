import unittest, re
from rexp.patterns import IPAddressPattern

class IpAddressPatternTestMethods(unittest.TestCase):
    def test_invalid(self):
        callable = IPAddressPattern()
        try:
            callable()
        except:
            self.assertTrue(1)

        try:
            callable('x5')
        except:
            self.assertTrue(1)

    def test_ipv4(self):
        callable = IPAddressPattern()
        expr = callable('v4')
        m = re.match(expr, '127.0.0.1')
        self.assertEqual(m.group(0), '127.0.0.1')

    def test_ipv6(self):
        callable = IPAddressPattern()
        expr = callable('v6')
        m = re.match(expr, '2001:0db8:0a0b:12f0:0000:0000:0000:0001')
        self.assertEqual(m.group(0), '2001:0db8:0a0b:12f0:0000:0000:0000:0001')
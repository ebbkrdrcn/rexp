import unittest, re
from rexp.patterns import KeyValuePairPattern

class KeyValuePairPatternTestMethods(unittest.TestCase):

    def test_pattern(self):
        callable = KeyValuePairPattern()
        expr = callable(capture_name='el')
        result = [m.groupdict() for m in re.finditer(expr, 'ManagedElement=BVI099,SystemFunctions=1,Fm=1,FmAlarm=1')]
        self.assertEqual(result, [
            {
                'el_key': 'ManagedElement',
                'el_value': 'BVI099',

            }, {
                'el_key': 'SystemFunctions',
                'el_value': '1',
            }, {
                'el_key': 'Fm',
                'el_value': '1',
            },
            {

                'el_key': 'FmAlarm',
                'el_value': '1',
            }
        ])


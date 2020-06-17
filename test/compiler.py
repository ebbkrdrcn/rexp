import unittest, re
from rexp.compiler import PatternCompiler


class CompilerTestMethods(unittest.TestCase):
    def test_compile_1(self):
        compiler = PatternCompiler(pattern_set=dict(
            TEST=r'\w+'
        ))

        try:
            c1 = compiler.compile('$1{TEST}')
        except Exception as exc:
            self.assertTrue(1)

        c1 = compiler.compile('$1{TEST}', ['test'])
        self.assertEqual(c1, r'(?:(?P<test>(\w+)))')

    def test_compile_2(self):
        compiler = PatternCompiler(pattern_set=dict(
            TEST=r'\w+'
        ))

        try:
            c1 = compiler.compile('$1{TEST}')
        except:
            self.assertTrue(1)

        c1 = compiler.compile('$1{TEST}', ['test'])
        self.assertEqual(c1, r'(?:(?P<test>(\w+)))')

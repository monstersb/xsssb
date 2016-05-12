import unittest
from xsssb import new_tokenizer

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_tokenize(self):
        self.assertEqual(new_tokenizer.tokenize_str_one('function'), ('function', 'function'))
        self.assertEqual(new_tokenizer.tokenize_str_one(' \nfunction '), ('function', 'function'))
        self.assertEqual(new_tokenizer.tokenize_str_one('0.10'), ('number', '0.10'))
        self.assertEqual(new_tokenizer.tokenize_str_one('10'), ('number', '10'))
        self.assertEqual(new_tokenizer.tokenize_str_one('1.23'), ('number', '1.23'))
        self.assertEqual(new_tokenizer.tokenize_str_one('1.23e+1'), ('number', '1.23e+1'))
        self.assertEqual(new_tokenizer.tokenize_str_one('1.23E-1'), ('number', '1.23e-1'))
        self.assertEqual(new_tokenizer.tokenize_str_one('23E-1'), ('number', '23e-1'))
        self.assertEqual(new_tokenizer.tokenize_str_one('23.E1'), ('number', '23.e1'))
        self.assertEqual(new_tokenizer.tokenize_str_one('0x12abcdef'), ('number', '0x12abcdef'))
        self.assertEqual(new_tokenizer.tokenize_str_one('0x980abcdFef'), ('number', '0x980abcdFef'))
        self.assertEqual(new_tokenizer.tokenize_str_one('0X980abcdFef'), ('number', '0x980abcdFef'))
        self.assertEqual(new_tokenizer.tokenize_str_one('0b10101'), ('number', '0b10101'))
        self.assertEqual(new_tokenizer.tokenize_str_one('0B10101'), ('number', '0b10101'))
        self.assertEqual(new_tokenizer.tokenize_str_one('0123'), ('number', '0123'))
        self.assertEqual(new_tokenizer.tokenize_str_one('0o123'), ('number', '0o123'))
        self.assertEqual(new_tokenizer.tokenize_str_one('0O123'), ('number', '0o123'))
        self.assertEqual(new_tokenizer.tokenize_str_one('monster'), ('identifier', 'monster'))
        self.assertEqual(new_tokenizer.tokenize_str_one('monster test'), ('identifier', 'monster'))
        self.assertEqual(new_tokenizer.tokenize_str_one('+='), ('addition_assignment', '+='))
        self.assertEqual(new_tokenizer.tokenize_str_one('/[\\w]+/'), ('regex', '/[\\w]+/'))


if __name__ == '__main__':
    unittest.main()

import unittest
from wc import WC


class TestWC(unittest.TestCase):
    def test_wc(self):
        wc = WC('D:/PyC/Projects/WC/example/test.py', '-c')
        self.assertEqual(wc.file_dict, 'D:/PyC/Projects/WC/example/test.py')
        self.assertEqual(wc.order, '-c')

    def test_chars_count(self):
        wc = WC('D:/PyC/Projects/WC/example/test.py', '')
        chars = wc.chars_count()
        self.assertEqual(chars, 407)

    def test_lines_count(self):
        wc = WC('D:/PyC/Projects/WC/example/test.py', '')
        lines = wc.lines_count()
        self.assertEqual(lines[0], 11)
        self.assertEqual(lines[1], 10)
        self.assertEqual(lines[2], 1)
        self.assertEqual(lines[3], 22)

    def test_words_count(self):
        wc = WC('D:/PyC/Projects/WC/example/test.py', '')
        words = wc.words_count()
        self.assertEqual(words, 75)

    def test_recur_files(self):
        test = ['1', 'test.py', 'test.txt', '1.txt', 'fish.py']
        wc = WC('D:/PyC/Projects/WC/example', '')
        result = wc.recur_files()
        for i in range(len(test)):
            self.assertEqual(result[i], test[i])

    def test_main_function(self):
        for order in ['-c', '-w', '-l', '-a', '-s',  '-x', '-a', '-g', ' ']:
            wc = WC('D:/PyC/Projects/WC/example/test.py', order)
            wc.main_function()


if __name__ == '__main__':
    unittest.main()


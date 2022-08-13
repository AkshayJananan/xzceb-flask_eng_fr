import unittest
from translator import englishtofrench
from translator import frenchtoenglish

class TestEnglish2French(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishtofrench("None"), '')
    def test2(self):
        self.assertNotEqual(englishtofrench(0), 0)
    def test3(self):
        self.assertEqual(englishtofrench('Thank you'), 'Je vous remercie')
    def test4(self):
        self.assertEqual(englishtofrench('Goodbye'), 'Au revoir')

class TestFrench2English(unittest.TestCase):
    def test5(self):
        self.assertNotEqual(frenchtoenglish("None"), '')
    def test6(self):
        self.assertNotEqual(frenchtoenglish(0), 0)
    def test7(self):
        self.assertEqual(frenchtoenglish('Je vous remercie'), 'Thank you')
    def test8(self):
        self.assertEqual(frenchtoenglish('Au revoir'),'Goodbye')
    
unittest.main()
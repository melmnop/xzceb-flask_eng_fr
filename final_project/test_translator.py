import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
  
  def test_english_to_french(self):
    self.assertEqual(english_to_french('hello'), 'bonjour')
    self.assertEqual(english_to_french('goodbye'), 'au revoir')
    self.assertEqual(english_to_french('good'), 'bien')
    self.assertNotEqual(english_to_french(0), 0)
    
  def test_french_to_english(self):
    self.assertEqual(french_to_english('bien'), 'good')
    self.assertEqual(french_to_english('au revoir'), 'goodbye')
    self.assertNotEqual(french_to_english(0), 0)
    self.assertEqual(french_to_english('bonjour'), 'hello')

if__name__ == '__main__'
    unittest.main()

import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
  
  def test_english_to_french(self):
    self.assertEqual(english_to_french('hello'), 'bonjour')
    self.assertEqual(english_to_french('good'), 'bien')
    self.assertNotEqual(english_to_french(0), 0)
    self.assertNotEqual(english_to_french('None'), '')
    
  def test_french_to_english(self):
    self.assertEqual(french_to_english('bien'), 'good')
    self.assertNotEqual(french_to_english(0), 0)
    self.assertNotEqual(french_to_english('None'), '')                    
    self.assertEqual(french_to_english('bonjour'), 'hello')

unittest.main()

import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
  
  def test_english_to_french(self):
    self.assertNotEqual(english_to_french('Hello'), 'Hello')
    self.assertNotEqual(english_to_french('NONE'), '')
    self.assertEqual(english_to_french('Hello'), 'Bonjour')
    self.assertNotEqual(english_to_french(0), 0)
    
  def test_french_to_english(self):
    self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
    self.assertNotEqual(french_to_english('NONE'), '')
    self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
    self.assertNotEqual(french_to_english(0), 0)
                        
unittest.main()


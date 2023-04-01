import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
  
  def test_english_to_french(self):
    self.assertNotEqual(english_to_french('hello'), 'hello')
    self.assertNotEqual(english_to_french(''), '')
    #self.assertEqual(english_to_french('hello'), 'bonjour')
    #self.assertNotEqual(english_to_french(0), 0)
    
    def test_french_to_english(self):
    self.assertNotEqual(french_to_english('bonjour'), 'bonjour')
    self.assertNotEqual(french_to_english(''), '')
    #self.assertEqual(french_to_english('au revoir'), 'goodbye')
    #self.assertNotEqual(french_to_english(0), 0)
                        
   
unittest.main()

import json
from ibm_watson import LanguageTranslatorV3

url_lt = 'https://gateway.watsonplatform.net/language-translator/api'

apiKey_lt = 'dfa7167f927b088baf2aa9285d5c68cb'
version_lt = '2018-05-01'

language_translator = LanguageTranslatorV3(iam_apikey = apikey_lt, url = url_lt, version = version_lt)

"""Functions use Wastson Translator to translate"""

def english_to_french(englishText):
  """Translates English to French"""
  translation_response = language_translator.translate(text = englishText, model_id = 'en-fr')
  translation = translation_response.get_result()
  french_translation = translation['translations'][0]['translation]
  return(french_translation)

def french_to_english(frenchText):
  """Translates French to English"""
  translation_response = language_translator.translate(text = frenchText, model_id = 'fr-en')
  translation = translation_response.get_result()
  english_translation = translation['translations'][0]['translation]
  return(english_translation)                                                  
                                                      

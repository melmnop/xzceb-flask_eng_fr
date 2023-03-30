"""Two functions that will use Watson Translator to translate"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

URL_LT = 'https://gateway.watsonplatform.net/language-translator/api'

APIKEY_LT = 'dfa7167f927b088baf2aa9285d5c68cb'
VERSION_LT = '2018-05-01'

language_translator = LanguageTranslatorV3(iam_apikey = APIKEY_LT, url = URL_LT, version = VERSION_LT)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')


def english_to_french(englishText):
    """Translates English to French"""
    translation_response = language_translator.translate(text = englishText, model_id = 'en-fr')
    translation = translation_response.get_result()
    french_translation = translation['translations'][0]['translation]
    return french_translation

def french_to_english(frenchText):
    """Translates French to English"""
    translation_response = language_translator.translate(text = frenchText, model_id = 'fr-en')
    translation = translation_response.get_result()
    english_translation = translation['translations'][0]['translation]
    return english_translation                                                                                                     

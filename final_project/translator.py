"""Two functions that will use Watson Translator to translate"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('lW5nKHZ-dascQb4ZpRVt-2XKz9HrCOK2wTiOaXTCxYeF')

language_translator = LanguageTranslatorV3(version = '2018-05-01', authenticator=authenticator)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/4ecc31ff-3cae-45d7-bb3b-13b99049deac')


def english_to_french(englishText):
    """Function translates English to French"""
    translation_response = language_translator.translate(text = englishText, model_id = 'en-fr')
    translation = translation_response.get_result()
    french_translation = translation['translations'][0]['translation']
    return french_translation

def french_to_english(frenchText):
    """Function translates French to English"""
    translation_response = language_translator.translate(text = frenchText, model_id = 'fr-en')
    translation = translation_response.get_result()
    english_translation = translation['translations'][0]['translation']
    return english_translation                                                                                                     

"""Two functions that will use Watson Translator to translate"""
#import json
#import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']
authenticator = IAMAuthenticator('lW5nKHZ-dascQb4ZpRVt-2XKz9HrCOK2wTiOaXTCxYeF')

language_translator = LanguageTranslatorV3(
    version = '2018-05-01', authenticator=authenticator)
language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/4ecc31ff-3cae-45d7-bb3b-13b99049deac')
                                
def english_to_french(english_text):
    """Function translates English to French"""
    translation = language_translator.translate(
    text = english_text, model_id = 'en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Function translates French to English"""
    translation = language_translator.translate(
    text = french_text, model_id = 'fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text 

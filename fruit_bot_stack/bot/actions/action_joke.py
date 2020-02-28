import logging
import requests
import json
from rasa_core_sdk import Action
from rasa_sdk.events import UserUtteranceReverted


class ActionJoke(Action):

    def name(self):
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        joke = self.get_joke()
        dispatcher.utter_message(text=joke) 
        return [UserUtteranceReverted()]

    @staticmethod
    def get_joke():
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)
        return request['value']

import logging
import requests
import json
from rasa_core_sdk import Action


class ActionJoke(Action):

    def name(self):
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        joke = self.get_joke()
        dispatcher.utter_message(text=joke) 
        return []

    @staticmethod
    def get_joke():
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)
        return request['value']

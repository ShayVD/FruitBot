from rasa_sdk.events import FollowupAction, SlotSet
from rasa_sdk.forms import FormAction

from actions.action_joke import ActionJoke


class FormInitialDetails(FormAction):
    """
    Gather users name and email
    """

    def name(self):
        return "form_initial_details"

    @staticmethod
    def required_slots(tracker):
        return ["PERSON", "EMAIL"]

    def slot_mappings(self):
        return {"PERSON": [self.from_text()], "EMAIL": [self.from_text()]}

    async def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Thank you!")
        first_name, last_name = self.get_first_last_name(tracker.get_slot("PERSON"))

        return [
            FollowupAction("utter_welcome"),
            SlotSet("first_name", first_name),
            SlotSet("last_name", last_name),
        ]

    def validate_PERSON(self, value, dispatcher, tracker, domain):
        response = None
        entity_present, entity_value = self.check_entity(
            "PERSON", tracker.latest_message["entities"]
        )
        intent = tracker.latest_message["intent"]["name"]
        if intent == "affirm":
            response = "utter_affirm_name"
        elif intent == "deny":
            response = "utter_deny_name"
        elif intent == "why":
            response = "utter_why_name"
        elif intent == "tell_joke":
            joke = ActionJoke().get_joke()
            dispatcher.utter_message(text=joke)
        elif entity_present:
            return {"PERSON": entity_value}
        else:
            dispatcher.utter_message(text="I don't understand that, sorry!")
        
        if response:
            dispatcher.utter_message(template=response) 

        return {"PERSON": None}

    def validate_EMAIL(self, value, dispatcher, tracker, domain):
        response = None
        entity_present, entity_value = self.check_entity(
            "EMAIL", tracker.latest_message["entities"]
        )
        intent = tracker.latest_message["intent"]["name"]
        if entity_present:
            return {"EMAIL":entity_value}
        elif intent == "affirm":
            response = "utter_affirm_email"
        elif intent == "deny":
            response = "utter_deny_email"
        elif intent == "why":
            response = "utter_why_email"
        elif intent == "tell_joke":
            joke = ActionJoke().get_joke()
            dispatcher.utter_message(text=joke)
        else:
            dispatcher.utter_message(text="I'm sorry I didn't quite catch that.")

        if response:
            dispatcher.utter_message(template=response) 

        return {"EMAIL": None}

    @staticmethod
    def get_first_last_name(name):
        names = name.split(" ")
        first_name = names[0]
        last_name = ""

        for i in range(1, len(names)):
            last_name += names[i] + " "

        return first_name, last_name

    @staticmethod
    def check_entity(entity, entities):
        for i in range(len(entities)):
            if entities[i]["entity"] == entity:
                return True, entities[i]["value"]
        return False, None

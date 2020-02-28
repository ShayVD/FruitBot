from rasa_sdk.events import FollowupAction, SlotSet
from rasa_sdk.forms import FormAction


class FormFruit(FormAction):
    """
    Gather fruit
    """

    def name(self):
        return "form_fruit"

    @staticmethod
    def required_slots(tracker):
        return ["fruit"]

    def slot_mappings(self):
        return {"fruit": [self.from_text()]}

    async def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="You'll be glad you picked our delicious fruit!")

        return [
            FollowupAction("utter_contact_soon"),
        ]

    def validate_fruit(self, value, dispatcher, tracker, domain):
        response = None
        entity_present, entity_value = self.check_entity(
            "fruit", tracker.latest_message["entities"]
        )
        intent = tracker.latest_message["intent"]["name"]
        if intent == "what_fruit":
            response = "utter_available_fruit"
        elif entity_present:
            return {"fruit": entity_value}
        elif value.lower() in self.fruit_db():
            return {"fruit": value.lower()}
        else:
            dispatcher.utter_message("Sorry I didn't catch that! Type the name of the fruit you're interested in buying.")
        
        if response:
            dispatcher.utter_message(template=response) 

        return {"fruit": None}

    @staticmethod
    def fruit_db():
        return [
            "apple",
            "apples",
            "orange",
            "oranges",
            "banana",
            "bananas",
            "strawberry",
            "strawberries",
            "kiwi",
            "kiwis",
        ]

    @staticmethod
    def check_entity(entity, entities):
        for i in range(len(entities)):
            if entities[i]["entity"] == entity:
                return True, entities[i]["value"]
        return False, None

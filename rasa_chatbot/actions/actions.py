from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import Any, Text, Dict, List
import re

class AddSubAction(Action):
    
    def name(self) -> Text:
        return "add_sub_action"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        y = tracker.events
        print(len(y))
        found_value = False
        for i in range(len(y), -1, -1):
            try:
                value = y[i]['parse_data']['entities'][0]['value']
                print(value)
                found_value = True
                break
            except:
                pass

        dispatcher.utter_message(f"your subscriptions added {value} days") 
        return []
class ShowPriceAndAffrim(Action):
    def name(self) -> Text:
        return "show_price_and_affrim"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        x = tracker.latest_message['entities']
        print(x)
        dispatcher.utter_message(f"its cost {int(x[0]['value']) * 2000} toman are you sure?") 
        return []

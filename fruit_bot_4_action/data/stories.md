## happy path
* greet
  - utter_greet
  - form_initial_details
  - form{"name": "form_initial_details"}
  - form{"name": null}
  - slot{"first_name": "Shay"}
  - slot{"last_name": "van Dam"}
  - utter_welcome
  - utter_ask_buy_fruit
* affirm OR want_fruit
  - form_fruit
  - form{"name": "form_fruit"}
  - form{"name": null}
  - utter_contact_soon

## happy path - deny fruit once
* greet
  - utter_greet
  - form_initial_details
  - form{"name": "form_initial_details"}
  - form{"name": null}
  - slot{"first_name": "Shay"}
  - slot{"last_name": "van Dam"}
  - utter_welcome
  - utter_ask_buy_fruit
* deny
  - utter_ask_buy_fruit_again
* affirm OR want_fruit
  - form_fruit
  - form{"name": "form_fruit"}
  - form{"name": null}
  - utter_contact_soon

## happy path - deny fruit twice
* greet
  - utter_greet
  - form_initial_details
  - form{"name": "form_initial_details"}
  - form{"name": null}
  - slot{"first_name": "Shay"}
  - slot{"last_name": "van Dam"}
  - utter_welcome
  - utter_ask_buy_fruit
* deny
  - utter_ask_buy_fruit_again
* deny
  - utter_ask_buy_fruit_again_again
* affirm OR want_fruit
  - utter_hard_bargain
  - form_fruit
  - form{"name": "form_fruit"}
  - form{"name": null}
  - utter_contact_soon

## happy path - deny fruit three times
* greet
  - utter_greet
  - form_initial_details
  - form{"name": "form_initial_details"}
  - form{"name": null}
  - slot{"first_name": "Shay"}
  - slot{"last_name": "van Dam"}
  - utter_welcome
  - utter_ask_buy_fruit
* deny
  - utter_ask_buy_fruit_again
* deny
  - utter_ask_buy_fruit_again_again
* deny
  - utter_done_asking
* affirm OR want_fruit 
  - form_fruit
  - form{"name": "form_fruit"}
  - form{"name": null}
  - utter_contact_soon

## unhappy path
* greet
  - utter_greet
  - form_initial_details
  - form{"name": "form_initial_details"}
  - form{"name": null}
  - slot{"first_name": "Shay"}
  - slot{"last_name": "van Dam"}
  - utter_welcome
  - utter_ask_buy_fruit
* deny
  - utter_ask_buy_fruit_again
* deny
  - utter_ask_buy_fruit_again_again
* deny
  - utter_done_asking

## Joke
* tell_joke
  - action_joke

## Are You a Bot
* bot_challenge
  - utter_iamabot

## Thanks
* thank
  - utter_no_problem

## Goodbye
* goodbye
  - utter_goodbye
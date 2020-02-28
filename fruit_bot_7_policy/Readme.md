## Changes
- config.yml - Extra policies added. 
- Added MappingPolicy and gave it a higher priority than FormPolicy so that the the Form would not need to be interrupted.
- Removed tell_joke intent from forms.
- Added EmbeddingPolicy. Set to 50 epochs. Used the MaxHistoryTrackerFeaturizer instead of the FullDialogueTrackerFeaturizer to shorten training time.
- Added FallbackPolicy. Defined the utter_deafult response in domain.yml.
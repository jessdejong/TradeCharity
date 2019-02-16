import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
import pprint

# setup API
natural_language_processing = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='VF3FzeOIqt7yesb3WDtvYRP283LjPFWBC37lOS19jbi8',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api')

# analyze text
def analyze(textString):
    response = natural_language_processing.analyze(
        text = textString,
        features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
            keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2))).get_result()
    data = json.loads(json.dumps(response, indent=2))
    return data

text='IBM is an American multinational technology company headquartered in Armonk, New York, United States, with operations in over 170 countries'
data = analyze(text);
#print(data)
pprint.pprint(data)

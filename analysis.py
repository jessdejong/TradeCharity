import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
import pprint
import news_wrapper
 
# setup API
natural_language_processing = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='VF3FzeOIqt7yesb3WDtvYRP283LjPFWBC37lOS19jbi8',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api')

def analyze(textString):
    """Analyzes sentiment of the text parameter using the IBM Watson API."""
    response = natural_language_processing.analyze(
        text = textString,
        features=Features(
            keywords=KeywordsOptions(emotion=False, sentiment=True, limit=1))).get_result()

    try:
        data = json.loads(json.dumps(response, indent=2))
        #pprint.pprint(data['keywords'][0]['sentiment']['score'])
        return data['keywords'][0]['sentiment']['score']
    except:
        return None

# text='IBM is a American multinational technology company headquartered in Armonk, New York, United States, terrible horrible does not work bad with operations in over 170 countries'
# analyze(text);


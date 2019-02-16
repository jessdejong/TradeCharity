import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
import pprint

'''
natural_language_processing = NaturalLanguageUnderstandingV1(
        username='a058b551-a067-48ad-9c08-3d57cb331a12',
        password='nW4Q8XpczFc4',
        version='2017-02-27')
'''

natural_language_processing = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='VF3FzeOIqt7yesb3WDtvYRP283LjPFWBC37lOS19jbi8',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api')

'''def getNewsTitles():
    tweets = twitter_wrapper.getUserTweets(username)
    urls = twitter_wrapper.getUserLinks(username)
'''

def analyze(titleText):
    response = natural_language_processing.analyze(
        text = titleText,
        features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
            keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2))).get_result()
    '''
        response = natural_language_understanding.analyze(

                text = titleText,

                features = Features(
                    keywords=KeywordsOptions(
                        emotion=True,
                        sentiment=True,
                        limit=1)),
                    
                language = 'en')
    '''
    data = json.loads(json.dumps(response, indent=2))
    return data

text='IBM is an American multinational technology company headquartered in Armonk, New York, United States, with operations in over 170 countries'
data = analyze(text);
#print(data)
pprint.pprint(data)

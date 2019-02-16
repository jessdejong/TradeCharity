import tweepy
import json

file = open("api.txt", "r")
with open("api.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

ACCESS_TOKEN = array[0].rstrip('\n')
ACCESS_SECRET = array[1].rstrip('\n')
CONSUMER_KEY = array[2].rstrip('\n')
CONSUMER_SECRET = array[3].rstrip('\n')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)


# def getUserTweets(username):
#     t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
#     data = json.loads(json.dumps(t.statuses.user_timeline(screen_name=username, count=10)))
#     tweets = [];
#     for i in range(len(data)):
#         tweets.append(data[i]["text"].encode('ascii',errors='ignore').decode())
#     return tweets
    
# def getUserFollowers(username):
#     t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
#     data = json.loads(json.dumps(t.friends.list(screen_name=username, count=100)))
#     friends = [];
#     for i in range(len(data["users"])):
#         friends.append(data["users"][i]["screen_name"])
#     return friends

# def getUserLinks(username):
#     t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
#     data = json.loads(json.dumps(t.statuses.user_timeline(screen_name=username, count=10)))
#     links = [];
#     for i in range(len(data)):
#         links.append("https://www.twitter.com/"+username+"/status/"+str(data[i]["id"]))
#     return links
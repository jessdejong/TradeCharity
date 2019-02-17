from flask import Flask, url_for, request, render_template, Markup, redirect
import news_wrapper
import trading
# import sentiment_analysis

app = Flask(__name__)

arr = news_wrapper.get_article_info()
for i in arr:
	print i

@app.route('/')
def home():
	return redirect('home')

@app.route('/home')
def display_template(username=None):
	return render_template('Home.html', username=username)

@app.route('/backtest/<year>/<month>/<day>', methods=['GET'])
def getBacktest(year, month, day):
    if request.method == 'GET':
        ret = trading.backtest(year, month, day)
        return ret
    else:
        return home()


# @app.route('/home/<username>', methods=['GET', 'POST'])
# def login(username):
# 	if request.method == 'GET':
# 		return ' ||| '.join(twitter_wrapper.getUserTweets(username))
# 	else:
# 		return hello()


# @app.route('/analysis/<username>', methods=['GET'])
# def ana(username):
# 	if request.method == 'GET':
# 		ret = ""
# 		# data = sentiment_analysis.find_negative_tweets(username)[0]
# 		# ret = " ".join(data) + "|||"

# 		# users = twitter_wrapper.getUserFollowers(username)
# 		# bad_tweets = []
# 		# for i in users:
# 		# 	bet = sentiment_analysis.find_negative_tweets(i)[0]
# 		# 	if(len(bet) >= 1):
# 		# 		bad_tweets.append(' '.join(bet))
# 		# ret = ret +  ' '.join(bad_tweets)
# 		return ret
# 	else:
# 		return hello()

'''with app.test_request_context():
	print url_for('hello_world')
	print url_for('projects')
	print url_for('about', next='/')
	print url_for('hello', username='SyedA')
	print url_for('static', filename='home.css') '''

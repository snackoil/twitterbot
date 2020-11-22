# Origin BOT https://github.com/0xGrimnir/Simple-Retweet-Bot/
# Author: Tyler L. Jones || CyberVox
# Date: Saturday, May 20th - 2017.
# License: MIT License.
# Tiny modification by Cyberpanda for @snackoil on twitter. 22.11.2020

import tweepy
from time import sleep

# Nope I don't share tokens neither keys :P
consumer_key = 'xxxxxxxx'
consumer_secret = 'xxxxxxxx'
access_token = 'xxxxxxxx'
access_secret = 'xxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def retweet(lookUpLastXtweets):
    for tweet in tweepy.Cursor(api.search, q='#snackoil').items(lookUpLastXtweets):
        try:
            print('\Snackoil Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
            tweet.retweet()
            print('Retweet published successfully.')
            sleep(10)
        except tweepy.TweepError as error:
            print('\nError. Retweet not successful. Reason: ')
            print(error.reason)
        except StopIteration:
            break

def autoFollow():
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print(follower.screen_name)

if __name__ == '__main__':
    try:
        retweet(50)
        autoFollow()
    except tweepy.TweepError:
        pass

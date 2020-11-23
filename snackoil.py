# Origin BOT https://github.com/0xGrimnir/Simple-Retweet-Bot/
# Author: Tyler L. Jones || CyberVox
# Date: Saturday, May 20th - 2017.
# License: MIT License.
#
# Tiny modifications by Cyberpanda for @snackoil on twitter.
import tweepy
from time import sleep
import sched, time
import os

consumer_key = 'xxxxxxxx'
consumer_secret = 'xxxxxxxx'
access_token = 'xxxxxxxx'
access_secret = 'xxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

s = sched.scheduler(time.time, time.sleep)

def retweet(lookUpLastXtweets):
    for tweet in tweepy.Cursor(api.search, q='#snackoil').items(lookUpLastXtweets):
        try:
            print('\nSnackoil Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')
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
        
def main(sc):
    try:
        print("# "*10+"Retweet"+" #"*10)
        retweet(5)
        print("# "*10+"AutoFollow"+" #"*10)
        autoFollow()
    except tweepy.TweepError:
        pass
    s.enter(20, 1, main, (sc,))

if __name__ == '__main__':
    for i in range(0, 11):
        os.system("clear" if os.name != "nt" else "cls")
        print(f"Brewing snakeoil.. {'🐍'*i} {i*10}%")
        sleep(0.5)
    print("OH YEAH, LET'S ROCK THIS!")
    s.enter(8, 1, main, (s,))
    s.run()

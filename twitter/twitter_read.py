# python 3
from twitter import *

# SETTING TWITTER ACCESS
token = ""
token_key = ""
con_secret = ""
con_secret_key = ""

auth = OAuth(token, token_key, con_secret, con_secret_key)
t = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))


# twitter read
def twitter_read():
    twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')
    for msg in twitter_userstream.user():
        print(msg)
        if 'user' in msg:
            if msg['user']['screen_name'] == 'inner_test':
                print(msg['text'])


# Main
if __name__ == '__main__':
    try:
        twitter_read()
    except:
        print("error")

from twitter import *

# SETTING TWITTER ACCESS
token = ""
token_key = ""
con_secret = ""
con_secret_key = ""

auth = OAuth(token, token_key, con_secret, con_secret_key)
t = Twitter(auth=auth)

# ダイレクトメッセージを送るユーザ
user_to_message = ''


# twitter write timeline
def twitter_write(tweet):
    # Update your status
    t.statuses.update(status=tweet)


# send direct message
def send_direct(message):
    t.direct_messages.new(user=user_to_message, text=message)


# Main
if __name__ == '__main__':
    twitter_write("hello")
    send_direct("hello")

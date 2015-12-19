from twitter import *
import serial
import time

# SETTING TWITTER ACCESS
token = ""
token_key = ""
con_secret = ""
con_secret_key = ""

auth = OAuth(token, token_key, con_secret, con_secret_key)
t = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))


# twitter read
def twitter_read():
    # init
    ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
    mg = ser.read()
    print(mg)

    twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')
    for msg in twitter_userstream.user():
        if 'user' in msg:
            # check user
            if msg['user']['screen_name'] == 'inner_test':
                print(msg['text'])

                cmd = msg['text'].split('-')
                if cmd[0] == 'light on':
                    sends = "l".encode()
                    ser.write(sends)
                elif cmd[0] == 'light off':
                    sends = "e".encode()
                    ser.write(sends)
                elif cmd[0] == 'stop':
                    sends = "s".encode()
                    ser.write(sends)
                elif cmd[0] == 'heating':
                    sends = "h".encode()
                    ser.write(sends)
                elif cmd[0] == 'cooling':
                    sends = "c".encode()
                    ser.write(sends)


# Main
if __name__ == '__main__':
    time.sleep(10)
    try:
        twitter_read()
    except:
        print("error")

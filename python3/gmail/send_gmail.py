
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# メイン関数
if __name__ == '__main__':

    msg = MIMEText('hello world!')
    me = 'hogehoge@gmail.com'
    you = 'hogehoge@hogehoge.com'

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = "test"
    msg['From'] = me
    msg['To'] = you

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(me, 'path')
    s.send_message(msg)
    s.close()



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib as smtp
from smtplib import SMTP
import time
from datetime import date
from sys import exit
from getpass import getpass

# Welcome Message
WELCOME_MESSAGE = """Hello, Welcome to the Customer Service Beater 5000!
Instructions:
    * Currently only gmail accounts are supported but you can change setupSMTP method to any 
      other host and port number. 
    * Change the textTemplate variable in the updateText() method to suit your needs.
      Note the example textTemplate if you want to incorporate the date and counter to your email
      content, it will be updated with every email sent. 
    * Run the script and answer the prompts.
    * The script will login via SMTP to gmail and will send an emails with the following logic:
        1. Initially - send a mail every 3 hours
        2. If 4 emails have been sent - decrease time interval by 15 minutes until the minimum time of 15 minutes is reached
    * Wait for customer service to give up or until the specified amount of emails is reached.
Hope this helps!
NOTE: Please allow less secure app logins to enable SMTP login: https://www.google.com/settings/security/lesssecureapps"""

# Constants
DEFAULT_NUMBER_OF_EMAILS = 10000
HOUR = 60*60
QUARTER_OF_AN_HOUR = 15*60
ERROR = -1

# This method updates the email content sent with the current date and a counter
# for how many emails have been sent.
def updateText(counter : int) -> str:
    textTemplate = f'''
    {date.today().strftime("%d/%m/%Y")}\n
        To whom it may concern,
        In regards to case number: XXXXX
        Following message {counter}, I would like to inform you that the case has yet to have been resolved to our satisfaction.
        Please contact us at XXXXXX to reach an agreeable conclusion.
        Thanks,
        '''
    return textTemplate

# MIME type of message - you can learn more about this at:
# https://docs.python.org/3/library/email.mime.html
def initializeMessage(myEmail : str, to : str, subject : str, text : str) -> MIMEMultipart:
    msg = MIMEMultipart()
    msg['From'] = myEmail
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    return msg

# Setup a secure session via SMTP
def setupSMTP(user, password) -> SMTP:
    try:
        server = smtp.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        return server
    except Exception as exception:
        print(f'Connection to SMTP server failed: {exception}')
        exit(ERROR)

# Sends an updated message every sleepTime interval.
# The sleepTime interval is dynamic and decreases by 15 minutes every 5 emails sent
# up to a minimum of 15 minutes.
def sendTimedMessage(server : SMTP, myEmail : str, to : str, subject : str ,counterLimit):
    counter = 1
    sleepTime = HOUR * 3    # Initially - send an email every 3 hours
    message = initializeMessage(myEmail, to, subject, updateText(counter))
    while counter < counterLimit:
        # SEND
        try:
            server.send_message(message)
            print(f'Message #{counter} sent successfully')
        except:
            print("Send message failed")

        # Reduce sleep interval by 15 minutes every 4 emails with a minimal interval of 15 minutes
        if sleepTime > QUARTER_OF_AN_HOUR and counter%4 == 0:
            print(f'Sent {counter} emails decreasing time interval')
            sleepTime -= QUARTER_OF_AN_HOUR

        # Randomize message and update counter
        del message
        counter += 1
        message = initializeMessage(myEmail, to, subject, updateText(counter))
        time.sleep(sleepTime)
    del message
    print('All messages sent')


def getUserInput():
    gmail_account = input("Please input your gmail address: ")
    gmail_password = getpass("Please input your password: ")
    to = input("To whom would you like to send emails (Please input an email address): ")
    subject = input("Please input subject: ")
    limit = input("How many emails would you like to send? ")
    try:
        limit = int(limit)
    except Exception as exception:
        print('You did not input a valid number, defaulting to 10,000')
        limit = DEFAULT_NUMBER_OF_EMAILS
    return {'user_email' : gmail_account, 'user_password' : gmail_password, 'subject' : subject ,'send_to_address' : to, 'counter_limit' : limit}


if __name__ == "__main__":
    print(WELCOME_MESSAGE)
    userData = getUserInput()
    server = setupSMTP(userData['user_email'], userData['user_password'])
    print("Connection to SMTP Successful")
    sendTimedMessage(server, userData['user_email'], userData['send_to_address'], userData['subject'], userData['counter_limit'])
    print('Task completed - closing session')
    server.close()

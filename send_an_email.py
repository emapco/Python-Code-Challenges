# Gmail API boilerplate imports
import base64
import os.path
from email.mime.text import MIMEText

from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# solution import
import smtplib

class Email:
    def __init__(self, sender="", receiver="", subject_line="", message_body=""):
        self.sender = sender
        self.receiver = receiver
        self.subject_line = subject_line
        self.message_body = message_body


def create_email(email):
    """Create a message for an email.

    Args:
        email: email object with sender, receiver, subject_line, and message_body
               attributes

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEText(email.message_body)
    message['to'] = email.receiver
    message['from'] = email.sender
    message['subject'] = email.subject_line
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_email(service, user_id, message):
    """Send an email message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message: Message to be sent.

    Returns:
      Sent Message.
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


SCOPES = ['https://mail.google.com/']
def main():
    """ Gmail API boilerplate
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # create service
    service = build('gmail', 'v1', credentials=creds)

    # create email object
    sender = "_@gmail.com"
    receiver = "_@gmail.com"
    subject_line = "Test From Python Email Script"
    message_body = "This is a test email sent from Python email script."
    email = Email(sender, receiver, subject_line, message_body)
    # Within the function, it calls the Gmail API to send an email
    send_email(service, 'me', create_email(email))


def solution():
    # these were parameters; they're included here for simplicity
    receiver = "_@gmail.com"
    subject = "Solution Test From Python Email Script"
    body = "This is a test email sent from Python email script."

    SENDER_EMAIL = "_@gmail.com"
    SENDER_PASSWORD = "PASSWORD"

    # format for email message to contain a subject line and message body
    message = "Subject: {}\n\n{}".format(subject, body)
    # opens secure connect to gmail smtp server on port 465
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        # login method to log in to sender's email account
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        # sends formatted email message from SENDER_EMAIL to receiver
        server.sendmail(SENDER_EMAIL, receiver, message)


if __name__ == '__main__':
    # main()
    # solution()
    pass

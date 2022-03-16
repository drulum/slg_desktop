import os
import smtplib
import ssl
from dotenv import load_dotenv
from email.message import EmailMessage


class ConstructEmail():

    def __init__(self) -> None:
        load_dotenv()
        self.email_config = {}
        self.email_config['host'] = os.getenv('SLG_EMAIL_HOST')
        self.email_config['port'] = os.getenv('SLG_EMAIL_PORT')
        self.email_config['user'] = os.getenv('SLG_EMAIL_USER')
        self.email_config['pass'] = os.getenv('SLG_EMAIL_PASS')
        self.email_config['from'] = os.getenv('SLG_EMAIL_FROM')
        self.email_config['to'] = os.getenv('SLG_EMAIL_TO')
        self.email_config['subject'] = os.getenv('SLG_EMAIL_SUBJECT')
        self.email_config['message'] = os.getenv('SLG_EMAIL_MESSAGE')
        self.data_file = None

    def generate_data_file(self):
        # TODO: write method once the format of the file is designed
        pass

    def send(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.email_config['host'], self.email_config['port'], context=context) as server:
            server.login(self.email_config['user'], self.email_config['pass'])
            msg = EmailMessage()
            msg.set_content(self.email_config['message'])  # may need to add .format(date=<variable passed for shopping list date>)
            msg['Subject'] = self.email_config['subject']  # may need to add .format(date=<variable passed for shopping list date>)
            msg['From'] = self.email_config['from']
            msg['To'] = self.email_config['to']
            # TODO: don't forget to attach the data file here
            server.send_message(msg)


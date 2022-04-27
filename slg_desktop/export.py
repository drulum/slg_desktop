import os
import smtplib
import ssl
from email.message import EmailMessage


class Export:

    def __init__(self, list_pk, delivery):
        self.list_pk = list_pk
        self.delivery = delivery

    def csv(self):
        deliver = getattr(self, self.delivery)
        deliver()

    def email(self):
        email_config = {}
        email_config['host'] = os.getenv('SLG_EMAIL_HOST')
        email_config['port'] = os.getenv('SLG_EMAIL_PORT')
        email_config['user'] = os.getenv('SLG_EMAIL_USER')
        email_config['pass'] = os.getenv('SLG_EMAIL_PASS')
        email_config['from'] = os.getenv('SLG_EMAIL_FROM')
        email_config['to'] = os.getenv('SLG_EMAIL_TO')
        email_config['subject'] = os.getenv('SLG_EMAIL_SUBJECT')
        email_config['message'] = os.getenv('SLG_EMAIL_MESSAGE')
        # data_file = None  # This will be supplied by the csv or json methods
        # context = ssl.create_default_context()
        # with smtplib.SMTP_SSL(email_config['host'], email_config['port'], context=context) as server:
        #     server.login(email_config['user'], email_config['pass'])
        #     msg = EmailMessage()
        #     msg.set_content(email_config['message'].format(date=for_date))
        #     msg['Subject'] = email_config['subject'].format(date=for_date)
        #     msg['From'] = email_config['from']
        #     msg['To'] = email_config['to']
        #     # TODO: don't forget to attach the data file here
        #     server.send_message(msg)
        print(email_config)

    def json(self):
        deliver = getattr(self, self.delivery)
        deliver()

    def save(self):
        print('Nothing to save yet.')


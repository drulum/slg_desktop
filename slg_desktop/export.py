import os
import smtplib
import ssl
from email.message import EmailMessage


class Export:

    def __init__(self, list_pk, delivery):
        self.list_pk = list_pk
        self.delivery = delivery
        # replace with correct date for shopping list
        self.list_date = '2023-09-01'
        self.file_name = None
        self.file_type = None

    def csv(self):
        self.file_type = 'csv'
        self.generate_file_name()
        deliver = getattr(self, self.delivery)
        deliver()

    def email(self):
        email_config = {'host': os.getenv('SLG_EMAIL_HOST'), 'port': int(os.getenv('SLG_EMAIL_PORT')),
                        'user': os.getenv('SLG_EMAIL_USER'), 'pass': os.getenv('SLG_EMAIL_PASS'),
                        'from': os.getenv('SLG_EMAIL_FROM'), 'to': os.getenv('SLG_EMAIL_TO'),
                        'subject': os.getenv('SLG_EMAIL_SUBJECT'), 'message': os.getenv('SLG_EMAIL_MESSAGE')}
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(email_config['host'], email_config['port'], context=context) as server:
            server.login(email_config['user'], email_config['pass'])
            msg = EmailMessage()
            msg.set_content(email_config['message'].format(date=self.list_date, filetype=self.file_type))
            msg['Subject'] = email_config['subject'].format(date=self.list_date)
            msg['From'] = email_config['from']
            msg['To'] = email_config['to']
            # TODO: don't forget to attach the generated file in place of the test
            with open(f'data/{self.file_name}', 'rb') as fp:
                file_data = fp.read()
            msg.add_attachment(file_data, maintype='text', subtype=self.file_type, filename=self.file_name)
            server.send_message(msg)

    def generate_file_name(self):
        self.file_name = f'{self.list_date}_shopping_list.{self.file_type}'

    def json(self):
        self.file_type = 'json'
        self.generate_file_name()
        deliver = getattr(self, self.delivery)
        deliver()

    def save(self):
        print('Nothing to save yet.')

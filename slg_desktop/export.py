import os
import smtplib
import ssl
from email.message import EmailMessage


class Export:

    def __init__(self, list_pk, delivery):
        self.list_pk = list_pk
        self.delivery = delivery
        self.filename = "test.csv"

    def csv(self):
        deliver = getattr(self, self.delivery)
        deliver()

    def email(self):
        # Get date and csv/json from mainwindow
        for_date = '2023-09-01'
        file_type = 'csv'

        email_config = {'host': os.getenv('SLG_EMAIL_HOST'), 'port': int(os.getenv('SLG_EMAIL_PORT')),
                        'user': os.getenv('SLG_EMAIL_USER'), 'pass': os.getenv('SLG_EMAIL_PASS'),
                        'from': os.getenv('SLG_EMAIL_FROM'), 'to': os.getenv('SLG_EMAIL_TO'),
                        'subject': os.getenv('SLG_EMAIL_SUBJECT'), 'message': os.getenv('SLG_EMAIL_MESSAGE')}
        # data_file = None  # This will be supplied by the csv or json methods
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(email_config['host'], email_config['port'], context=context) as server:
            server.login(email_config['user'], email_config['pass'])
            msg = EmailMessage()
            msg.set_content(email_config['message'].format(date=for_date, filetype=file_type))
            msg['Subject'] = email_config['subject'].format(date=for_date)
            msg['From'] = email_config['from']
            msg['To'] = email_config['to']
            # TODO: don't forget to attach the generated file in place of the test
            with open('data/test.csv', 'rb') as fp:
                file_data = fp.read()
            msg.add_attachment(file_data, maintype='text', subtype='csv', filename=self.filename)
            server.send_message(msg)

    def json(self):
        deliver = getattr(self, self.delivery)
        deliver()

    def save(self):
        print('Nothing to save yet.')

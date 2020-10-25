
import os
import sys
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

key = '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'

def send_mail(text):
    message = Mail(
        from_email='yayafer428@zuperholo.com',
        to_emails='vhpraneeth2001@gmail.com',
        subject='Contact - from portfolio',
        html_content=text.replace('\n', '<br/>')
    )

    try:
        sg = SendGridAPIClient(key)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print('Failed to send email')


# https://sendgrid.com/docs/for-developers/sending-email/v3-python-code-example/

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from mb_demopro import settings


def send_otp(email, otp):
    mail_content = "Hello,<br><strong>" + otp + "</strong> is your otp for verification.<br>Please do not share with " \
                                                "anyone. "
    message = Mail(
        from_email='test@gmail.com',  # change the mail
        to_emails=email,
        subject='OTP',
        html_content=mail_content
    )
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

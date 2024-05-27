''''
Email Sending using smtplib library
https://stackoverflow.com/questions/70261815/smtplib-smtpauthenticationerror-534-b5-7-9-application-specific-password-req
'''

import smtplib

def send_email(sender_email, recipient_email, password, subject, body):
    try:
        # Connect to the SMTP server
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()  # Secure the connection

        # Log in to the SMTP server
        smtp_server.login(sender_email, password)

        # Construct the email message
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        smtp_server.sendmail(sender_email, recipient_email, message)
        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email. Error: {e}")

    finally:
        # Quit the SMTP session
        smtp_server.quit()

# Email details
sender_email = 'haris7991@gmail.com'
recipient_email = 'nukhan@mail.com, khan.nafees.u@gmail.com'
password = 'pbnv pgsp fqvx rcfb'  # Enter your email password here
subject = 'Sending this email via Python Code TEST'
body = 'Check out my new medium article give it a like please na https://medium.com/@haris7991/building-an-smtp-email-sending-application-w-python-c5fa468e76cf'

# Send the email
send_email(sender_email, recipient_email, password, subject, body)


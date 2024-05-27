''''
Email Sending using smtplib library

Links: https://stackoverflow.com/questions/70261815/smtplib-smtpauthenticationerror-534-b5-7-9-application-specific-password-req
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
sender_email = 'sender-email-here'
recipient_email = 'recipient-email-here'
password = 'your-app-password'  # Enter your email password here
subject = 'subject-here'
body = 'content-message-here'

# Send the email
send_email(sender_email, recipient_email, password, subject, body)


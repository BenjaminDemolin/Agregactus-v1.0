import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""
    File name: aa_mail_function.py
    Description: This file contains email functions 
"""

"""
    Description: Send an email using Gmail
    Parameters:
        sender_email: Sender's email
        sender_password: Sender's password
        receiver_email: Receiver's email
        subject: Email's subject
        body: Email's body
    Return: True if the email is sent, False otherwise
"""
def send_email_gmail(sender_email, sender_password, receiver_email, subject, body):
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject

        # Attach the body of the email
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server (Gmail in this case)
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Start TLS for security
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return True
    except Exception as e:
        print(e)
        return False



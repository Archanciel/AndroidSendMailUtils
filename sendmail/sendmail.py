from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib


def sendemail(email_name, email_user, email_pswd, mailto, mailbcc, subject, body):
    # DON'T CHANGE THIS!
    # ...unless you're rewriting this script for your own SMTP server!
    smtp_server = 'smtp.mail.yahoo.com'
    smtp_port = 465

    # Build an SMTP compatible message
    # Note special utf-8 settings for subject and body !
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['To'] = mailto
    msg['From'] = email_name + " <" + email_user + ">"
    msg.attach(MIMEText(body, _charset="UTF-8"))

    toaddrs = [mailto] + [mailbcc]

    # Attempt to connect and send the email
    try:
        smtpObj = ''  # Declare within this block.
        # Check for SMTP over SSL by port number and connect accordingly
        if (smtp_port == 465):
            smtpObj = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:
            smtpObj = smtplib.SMTP(smtp_server, smtp_port)
        smtpObj.ehlo()
        # StartTLS if using the default TLS port number
        if (smtp_port == 587):
            # smtpObj.starttls()
            smtpObj.ehlo
        # Login, send and close the connection.
        smtpObj.login(email_user, email_pswd)
        smtpObj.sendmail(email_user, toaddrs, msg.as_string())
        smtpObj.close()
        return 1  # Return 1 to denote success!
    except Exception as err:
        # Print error and return 0 on failure.
        print(err)
        return 0


def sendemailTextAndHtml(email_name, email_user, email_pswd, mailto, mailbcc, subject, bodyTxt, bodyHtml):
    # DON'T CHANGE THIS!
    # ...unless you're rewriting this script for your own SMTP server!
    smtp_server = 'smtp.mail.yahoo.com'
    smtp_port = 465

    # Build an SMTP compatible message
    # Note special utf-8 settings for subject and body !
    #  msg = MIMEMultipart('alternative') causes the connection to close !!b
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['To'] = mailto
    msg['From'] = email_name + " <" + email_user + ">"
    msg.attach(MIMEText(bodyTxt, _charset="UTF-8"))
    msg.attach(MIMEText(bodyHtml, 'html'))

    toaddrs = [mailto] + [mailbcc]

    # Attempt to connect and send the email
    try:
        smtpObj = ''  # Declare within this block.
        # Check for SMTP over SSL by port number and connect accordingly
        if (smtp_port == 465):
            smtpObj = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:
            smtpObj = smtplib.SMTP(smtp_server, smtp_port)
        smtpObj.ehlo()
        # StartTLS if using the default TLS port number
        if (smtp_port == 587):
            # smtpObj.starttls()
            smtpObj.ehlo
        # Login, send and close the connection.
        smtpObj.login(email_user, email_pswd)
        smtpObj.sendmail(email_user, toaddrs, msg.as_string())
        smtpObj.close()
        return 1  # Return 1 to denote success!
    except Exception as err:
        # Print error and return 0 on failure.
        print(err)
        return 0


def sendemailHtml(email_name, email_user, email_pswd, mailto, mailbcc, subject, bodyHtml):
    # DON'T CHANGE THIS!
    # ...unless you're rewriting this script for your own SMTP server!
    smtp_server = 'smtp.mail.yahoo.com'
    smtp_port = 465

    # Build an SMTP compatible message
    # Note special utf-8 settings for subject and body !
    #  msg = MIMEMultipart('alternative') causes the connection to close !!b
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['To'] = mailto
    msg['From'] = email_name + " <" + email_user + ">"
    msg.attach(MIMEText(bodyHtml, 'html'))

    toaddrs = [mailto] + [mailbcc]

    # Attempt to connect and send the email
    try:
        smtpObj = ''  # Declare within this block.
        # Check for SMTP over SSL by port number and connect accordingly
        if (smtp_port == 465):
            smtpObj = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:
            smtpObj = smtplib.SMTP(smtp_server, smtp_port)
        smtpObj.ehlo()
        # StartTLS if using the default TLS port number
        if (smtp_port == 587):
            # smtpObj.starttls()
            smtpObj.ehlo
        # Login, send and close the connection.
        smtpObj.login(email_user, email_pswd)
        smtpObj.sendmail(email_user, toaddrs, msg.as_string())
        smtpObj.close()
        return 1  # Return 1 to denote success!
    except Exception as err:
        # Print error and return 0 on failure.
        print(err)
        return 0


import sys
import android
import pickle

droid = android.Android()

mailto = 'jp.schnyder@gmail.com'
mailbcc = 'jp.schnyder@gmail.com'
subject = 'essai subject'
bodyTxt = 'essai body text'
bodyHtml = """
<html>
 <head></head>
 <body>
  <p>Hi HTML freaks<br> How are you?<br> 
  Here is the <a href="https://www.python.org">link</a> you wanted. </p>
 </body>
</html> """
FILE_PATH = "sdcard/file.bin"

with open(FILE_PATH, 'rb') as handle:
    cred = pickle.loads(handle.read())


def sendMailWithBodyTo(bodyText, targetEmail, mailbcc, mailSubject, mailName):
    if (sendemail(mailName, cred['usr'], cred['pw'], targetEmail, mailbcc, mailSubject, bodyText)):
        pass
    else:
        # Exit with error if email is not sent successfully
        droid.makeToast('email failed')
        sys.exit(1)


def sendMailWithTxtAndHtmlBodyTo(bodyText, bodyHtml, targetEmail, mailbcc, mailSubject, mailName):
    if (sendemailTextAndHtml(mailName, cred['usr'], cred['pw'], targetEmail, mailbcc, mailSubject, bodyText, bodyHtml)):
        pass
    else:
        # Exit with error if email is not sent successfully
        droid.makeToast('email failed')
        sys.exit(1)


def sendMailWithHtmlBodyTo(bodyHtml, targetEmail, mailbcc, mailSubject, mailName):
    if (sendemailHtml(mailName, cred['usr'], cred['pw'], targetEmail, mailbcc, mailSubject, bodyHtml)):
        pass
    else:
        # Exit with error if email is not sent successfully
        droid.makeToast('email failed')
        sys.exit(1)


if __name__ == "__main__":
    # Send email 
    if (sendemailTextAndHtml('essai', cred['usr'], cred['pw'], mailto, mailbcc, subject, bodyTxt, bodyHtml)):
        #    if (sendemail('essai', cred['usr'], cred['pw'], mailto, mailbcc, subject, bodyTxt)):
        sys.exit(0)
    else:
        # Exit with error if email is not sent successfully
        droid.makeToast('email failed')
        sys.exit(1)

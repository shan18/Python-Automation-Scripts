import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import credentials


def get_contacts(filename):
    """
    Function to get all the name and email IDs of contacts in separate lists
    :param filename: File containing contact list
    :return: lists containing names and emails
    """
    names = []
    emails = []
    with open(filename, encoding='utf-8') as contacts_file:
        for contact in contacts_file:
            names.append(contact.split()[0])
            emails.append(contact.split()[1])
    return names, emails


def read_template(filename):
    """
    Returns a template comprising the contents of a file
    :param filename: File containing the email message
    :return: Template object
    """
    with open(filename, encoding='utf-8') as template_file:
        template = template_file.read()
    return Template(template)


def main():
    # get names and contact list
    names, emails = get_contacts('my_contacts.txt')
    message_template = read_template('message.txt')

    # setup the SMTP server
    server = smtplib.SMTP(credentials.HOST_NAME, credentials.PORT)
    server.ehlo()
    server.starttls()
    server.login(credentials.ADDRESS, credentials.PASSWORD)

    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        # add the person name to the title
        message = message_template.substitute(PERSON_NAME=name.title())

        # setup the message parameters
        msg['From'] = credentials.ADDRESS
        msg['To'] = email
        msg['Subject'] = 'Automated Email Sending with Python'

        # add the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server setup earlier
        server.send_message(msg)
        # server.sendmail(credentials.ADDRESS, 'thegeek.004@gmail.com', 'Hello')
        del msg

    # terminate the SMTP session and close the connection
    server.quit()


if __name__ == '__main__':
    main()

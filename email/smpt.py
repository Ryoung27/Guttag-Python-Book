import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

smtp_object.ehlo()

smtp_object.starttls()

# password = getpass.getpass('Password please: ')

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email,password)

from_address = email
to_address = input("Send too? ")
subject = input("enter the subject line: ")
message = input("end the body message: ")
msg = "Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address, to_address, msg)
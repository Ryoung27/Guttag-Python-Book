import imaplib
import getpass

M = imaplib.IMAP4_SSL('imap.gmail.com')

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")

M.login(email, password)

M.list()

M.select('inbox')

typ, data = M.search(None, 'SUBJECT "test"')
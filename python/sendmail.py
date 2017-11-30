#!/usr/bin/env python
import smtplib
from datetime import datetime

t = datetime.now()

#information
info = ''
info += ('\n'+u'test time is : '+'\n')
info += ('\n'+str(t)+'\n')
info += ('cna is stupid')
print(t)

gmail_user = 'logan@cyber00rn.org'
gmail_pwd = 'QWE!rty1'

smtpserver = smtplib.SMTP('smtp.googlemail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
#login
smtpserver.login(gmail_user, gmail_pwd)

#sender
fromaddr = "logan@cyber00rn.org"
#receive can be list
toaddrs = ['chocoowl@gmail.com', '']

#Subject
msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n" % (fromaddr, ", ".join(toaddrs), u'test'))

smtpserver.sendmail(fromaddr, toaddrs, msg+info)

#logout
smtpserver.quit()

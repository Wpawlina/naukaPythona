import smtplib


host='smtp.gmail.com'
port=465
user='server.wojciech@gmail.com'
password='zhrtvdastmhejivv'
mailFrom='Your automation system'
mailTo=['testowe@gmail.com','test@wp.pl']
mailBody='This is python email'
message = '''From: {}
Subject: {}
{}
'''.format(mailFrom,'Test mail',mailBody)

try:
    server=smtplib.SMTP_SSL(host,port)
    server.ehlo()
    server.login(user,password)
    server.sendmail(mailFrom,mailTo,message)
    server.close()
    print('mail sent')

except:
   print('error sending email')
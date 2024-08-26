import smtplib
import functools
import requests
import os   


host='smtp.gmail.com'
port=465
user='server.wojciech@gmail.com'
password='zhrtvdastmhejivv'
mailFrom='Your automation system'
mailTo=['tses@gmail.com','test@wp.pl']
mailBody='This is python email'


def SendEmail(host,port,user,password,mailFrom,mailTo,mailSubject,mailBody):
    message = '''From: {}
Subject: {}
{}
'''.format(mailFrom,mailSubject,mailBody)


    try:
        server=smtplib.SMTP_SSL(host,port)
        server.ehlo()
        server.login(user,password)
        server.sendmail(mailFrom,mailTo,message)
        server.close()
        print('mail sent')

    except:
        print('error sending email')
        return False
    
SendInfoEmail=functools.partial(SendEmail,host,port,user,password,mailSubject='Test mail 3')
SendInfoEmail(mailFrom=mailFrom,mailTo=mailTo,mailBody=mailBody)

 
 
def save_url_file(url, dir, file,msg):
       
    print(msg.format(file))
    
    r = requests.get(url, stream = True) 
    file_path = os.path.join(dir, file)
      
    with open(file_path, "wb") as f: 
        f.write(r.content)


msg = "Please wait - the file {} will be downloaded"
url = 'http://mobilo24.eu/spis'
dir = os.path.join(os.getcwd(), 'srednio zaawansowany\\contentOfwebsites')
file = 'spis.html'


SaveUrlToFile=functools.partial(save_url_file,dir=dir,msg='Please wait - the file {} will be downloaded')
SaveUrlToFile(url=url,file=file)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
file = 'logo.png'
SaveUrlToFile(url=url,file=file)


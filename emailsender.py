from smtplib import SMTP
gmail = input('enter your gmail!\n')
password = input('please enter your Gmail password\n')
message = input("please enter your message\n")
#gmail = input("please enter your email address!\n")
#password = input('what is your password?\n')
f= open('path/file','r')
#message = input('input your message to be sent?')
b=f.readlines()
print(b)
for x in b:
        print(x)
        li=1
        mailto = x
        msg= 'Dear '+x+'!\n'+message+'\n In regards!\n'+gmail
        mailServer = SMTP('smtp.gmail.com',587)
        mailServer.starttls()
        mailServer.login(gmail,password)
        print('sending email to'+mailto+'\n')
        mailServer.sendmail(gmail,mailto,msg)
        print(li)
        print('\n successfully sent to '+mailto)
        li=li+1
        mailServer.quit()
f.close()
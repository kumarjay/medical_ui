import yaml
import datetime
from email.message import EmailMessage
import smtplib


file = open("config.yaml", "r")
cfg = yaml.safe_load(file)

contacts= cfg['email']['contacts']
id= cfg['email']['id']
password= cfg['email']['password']


def send_mail(name, email, phone, date, doctor=None, department=None, message=None):
    # contacts= ['amrita@mirrag.com', 'abhishek@mirrag.com', 'prasanna@mirrag.com', 'kumarjay2107@gmail.com', 'jay.kumar@mirrag.com']
    # contacts= ['jay.kumar@mirrag.com']

    msg= EmailMessage()
    msg['Subject']= 'Appointment Detail'
    msg['From']= id
    msg['To']= ', '.join(contacts)
    # msg['To']= 'kumarjay2107@gmail.com'
    msg.set_content(f'One patient has booked an appointment for {date}, \nDoctor : {doctor}, Department : {department}. \nPatient Details : '
                    f'\nName : {name} \nEmail : {email} \nPhone : {phone} \nMessage: {message}')

    # with open(image_path, 'rb') as f:
    #     file_data= f.read()
    #     # file_type= imghdr.what(f.name)
    #     file_name= f.name
    #     print('img ', image_path, ' ', file_name)

    # msg.add_attachment(file_data, maintype='image', subtype= file_type, filename= file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
            smtp.login(id, password)
            smtp.send_message(msg)

            return True
        # print(contacts, ' ', email, ' ', password)
        # print('msg is..', msg)
        # print(2/0)
        # return True
    except:
        print('check your connection')
        return False

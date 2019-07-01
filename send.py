from flask import Flask 
from flask_mail import Mail, Message
import os
import test
from flask_cors import CORS, cross_origin
import base64
import json

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "gunnalert@gmail.com",
    "MAIL_PASSWORD": "omgvkmebzdazcavk"
}

app.config.update(mail_settings)
mail = Mail(app)

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

tri = Person("Tri Do","tricaodo1903@gmail.com")
theanh = Person("Anh Nguyen","tintheanh@gmail.com")
#beanh = Person("Anh Dinh","extramsj@gmail.com")
#emily = Person("Emily Laih","aemilylaih@gmail.com")
#nguyen = Person("Nguyen Dinh","leakim.foto@gmail.com")

users = [tri,theanh]

def dosomething():
    return "This is the do something method"


def send_email(mes1, mes2, mes3, img_data):
        img_data = img_data.replace("data:image/jpeg;base64,","")
        with app.app_context():
            with open("shooter.jpg","wb") as fh:
                fh.write(base64.b64decode(img_data))
            for user in users:
                message = "Location: "+mes1 + "\n\nDescription: "+mes3+'\n\n' + "Date and Time: "+mes2 + "\n\nPlease move to the nearest safe location away from the incident. For emergency, please dial 911.\n\nThe Gunnalert Team"
                subject = "ALERT, %s" % user.name
                msg = Message(sender=app.config.get("MAIL_USERNAME"),
                            recipients=[user.email],
                            body=message,
                            subject=subject)
                
                with app.open_resource("shooter.jpg") as fp:
                    msg.attach("shooter.jpg", "shooter/jpg", fp.read())
                mail.send(msg)
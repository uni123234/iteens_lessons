from flask import Flask
from flask_mail import Mail, Message
from secret import email, password

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.ukr.net"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = email
app.config["MAIL_PASSWORD"] = password
app.config["MAIL_DEFAULT_SENDER"] = email
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

mail = Mail(app)
app.app_context().push()

def send_email():
    msg = Message("Event reminder")
    msg.recipients = ["yatsura.andriy@ukr.net"]
    msg.body = "Test mail"
    msg.html = "<h1> Hello my friend </h1>"
    mail.send(msg)
    print("Email sent")

@app.route("/mail")
def mails():
    send_email()
    return f"Email sent"

app.run()

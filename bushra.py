import sendgrid
from datetime import date, timedelta
from db import config
import ideas

sendgrid = sendgrid.SendGridClient(
    config["SendGrid"]["API_User"],
    config["SendGrid"]["API_Key"],
)

emails = []
message = sendgrid.Mail()

for idea in ideas.get_tweeted(date.today() - timedelta(days=7)):
	emailbody += "whatever plus ideas"

for user in users.get_all():
	emails.append(user['email'])

message.set_from("xyz@IdeaBin.com")
message.add_to(emails)
message.set_subject("Weekly Newsletter for IdeaBin")
message.set_html(emailbody)

sendgrid.send(message)

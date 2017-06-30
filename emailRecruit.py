#!/usr/bin/python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

# Function to read template mail from mailTemplate and replace generic strings with Company specific values
# Takes Name, Company, Position as arguments
# Returns Mail Body
def getBody(name, company, position):
    try:
        file = open("mailTemplate", "r")
        body = file.read()
        file.close()
        return body.replace("$insertName$", name).replace("$insertCompany$", company).replace("$insertPosition$", position)
    except IOError:
        print "Error: File does not seem to exist."
        return "Hello"

fromaddr = "danisfermijohn@gmail.com"
toaddr = "dfermi@ncsu.edu"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Fall 2017 Full Time Application"

body = getBody("Name","Company","Position")
msg.attach(MIMEText(body, 'plain'))

filename = "resume.pdf"
attachment = open("resume.pdf", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "YOUR PASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
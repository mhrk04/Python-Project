# import library
from cgitb import html
from email.message import EmailMessage
from app_pass import password
import ssl
import smtplib

Sender ="haziqrohaizan@gmail.com"
SenderPass = password
Receiver = ["haziq.rohaizan@s.unikl.edu.my","m-4496742@moe-dl.edu.my"]

Subject = "Website Promote - mhaziqrk.uk"
MailBody = """
<html>
<head></head>
<body>
<h1>Website Promote for Haziq Rohaizan</h1>
<center><img src="https://mhaziqrk.uk/favicon.ico">
<video width="320" height="240" controls>
  <source src="https://www.youtube.com/watch?v=wDkjWSt3HOM">
  Your browser does not support the video tag.
</video>
</center>
<p>Hello Unikl MIIT Students,</p><br>
<p>I would like to invite you visit our new website. You can click link bellow</p><br>
<a href="https://mhaziqrk.uk">Click Here</a>
</body>
</html>
"""

# create instant

em = EmailMessage()
em['From']= Sender
em['To'] = Receiver
em['subject'] = Subject
em.add_header('Content-Type','text/html')
em.set_payload(MailBody)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
  smtp.login(Sender,SenderPass)
  smtp.sendmail(Sender,Receiver,em.as_string())

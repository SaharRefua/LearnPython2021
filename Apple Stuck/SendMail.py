# import smtplib, ssl
#
# smtp_server = "myMail@gmail.com"
# port = 587  # For starttls
# sender_email = "myMail@gmail.com"
# password = "MyPassword"#input("Type your password and press enter: ")
#
# # Create a secure SSL context
# context = ssl.create_default_context()

# Try to log in to server and send email
# try:
#     server = smtplib.SMTP(smtp_server,port)
#     server.ehlo() # Can be omitted
#     server.starttls(context=context) # Secure the connection
#     server.ehlo() # Can be omitted
#     server.login(sender_email, password)
#     # Send email here
# except Exception as e:
#     # Print any error messages to stdout
#     print(e)
# finally:
#     server.quit()
# import smtplib, ssl
# import socket
# socket.getaddrinfo('127.0.0.1', 8080)
# port = 465  # For SSL
# smtp_server = "myMail@gmail.com"
# sender_email = "myMail@gmail.com"  # Enter your address
# receiver_email = "myMail@gmail.com"  # Enter receiver address
# password = "MyPassword" # input("Type your password and press enter: ")
# message = """\
# Subject: Hi there
#
# This message is sent from Python."""
# if (use_proxy):
#     proxy = req.ProxyHandler({'https': proxy_url})
#     auth = req.HTTPBasicAuthHandler()
#     opener = req.build_opener(proxy, auth, req.HTTPHandler)
#     req.install_opener(opener)
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)







import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Python"
body = "This is a test email form Python!"
sender_email = "ragnar.vikings.xxx@gmail.com"
receiver_email = "refua.sahar@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")
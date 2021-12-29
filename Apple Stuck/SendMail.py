# import smtplib, ssl
#
# smtp_server = "refua.sahar@gmail.com"
# port = 587  # For starttls
# sender_email = "refua.sahar@gmail.com"
# password = "IZm9701!@"#input("Type your password and press enter: ")
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
#     # TODO: Send email here
# except Exception as e:
#     # Print any error messages to stdout
#     print(e)
# finally:
#     server.quit()
import smtplib, ssl
import socket
socket.getaddrinfo('127.0.0.1', 8080)
port = 465  # For SSL
smtp_server = "sahar.python.test@gmail.com"
sender_email = "sahar.python.test@gmail.com"  # Enter your address
receiver_email = "refua.sahar@gmail.com"  # Enter receiver address
password = "Sr6077517!#%" # input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""
if (use_proxy):
    proxy = req.ProxyHandler({'https': proxy_url})
    auth = req.HTTPBasicAuthHandler()
    opener = req.build_opener(proxy, auth, req.HTTPHandler)
    req.install_opener(opener)
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
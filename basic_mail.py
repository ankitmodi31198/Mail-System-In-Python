from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = 'smtp.gmail.com'
port = 587
username = "ankitmodi31198@gmail.com"
password = "*************"
from_list = username
to_list = ["modiankit.pal@gmail.com"]
try:
    email_con = smtplib.SMTP(host, port)
    print(email_con.ehlo())
    print(email_con.starttls())
    print(email_con.login(username, password))

    msg = MIMEMultipart("alternative")
    msg['subject'] = "Hello There Spartas!!"
    msg["From"] = from_list
    msg["To"] = to_list[0]
    plain_txt = "We are so glad to see you here!!"
    html_txt = """
    <html>
        <head>
            <title>Testing</title>
        </head>
        <body>
            <p>Hey! <br>We are <b>testing</b> this email made by <a href=#>html tags</a>.</p>

        </body>
    </html>"""

    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, 'html')

    msg.attach(part_1)
    msg.attach(part_2)

    # print(msg.as_string())

    print(email_con.sendmail(from_list, to_list, msg.as_string()))
    print(email_con.quit())

except smtplib.SMTPAuthenticationError:
    print("Error loading message")

except smtplib.SMTPException:
    print("Error loading message")
import smtplib

host = "smtp.gmail.com"
port = 587
username = "ankitmodi31198@gmail.com"
password = "************"

from_email = [username]
to_mail = ["modiankit.pal@gmail.com"]

email_conn = smtplib.SMTP(host, port)
print(email_conn)
print(email_conn.ehlo())
print(email_conn.starttls())
print(email_conn.login(username, password))
print(email_conn.sendmail(from_email, to_mail, "Hello there is an email message."))
print(email_conn.sendmail(from_email, to_mail, "Hello there is a second email message."))
print(email_conn.quit())

print("-*-*-*-*-*-*-*-*-*-*-*-*Second Method-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

from smtplib import SMTP

mail = SMTP(host, port)
mail.ehlo()
mail.starttls()
mail.login(username, password)
mail.sendmail(from_email, to_mail, "Hello There spartanss!!!")
mail.quit()
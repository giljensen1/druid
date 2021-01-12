import subprocess
import smtplib
from email.mime.text import MIMEText

threshold = 40
partition = "/"

def report_via_email():
 msg = MIMEText("Server running out of disk space")
 msg["Subject"] = "Low disk space warning"
 msg["From"] = "admin@example.com"
 msg["To"] = "gil.jensen@gmail.com"
 with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls()
    server.login("gil.jensen@gmail.com","UllrSon2")
    server.sendmail("admin@example.com", "gil.jensen@gmail.com", msg.as_string())

def check_once():
 df = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE)
 for line in df.stdout:
    splitline = line.decode().split()
    if splitline[5] == partition:
        if int(splitline[4][:-1]) > threshold:
            report_via_email()
check_once()

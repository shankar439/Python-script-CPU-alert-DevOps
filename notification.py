import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'sender@gmail.com'
receiver = 'receiver@gmail.com'
password = 'googleAppPassword'
port = 587
smtp_server = 'smtp.gmail.com'
subject = "High RAM Utilization Alert"
body = """
The RAM usage spiked please verify and do needed action in the server.
"""

def send_mail():
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP(smtp_server,port)
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender, receiver, message.as_string())
    server.quit()

print(psutil.cpu_percent(interval=5))

if __name__ == '__main__':
    ramUsage = psutil.virtual_memory().percent
    print(ramUsage)
    if ramUsage > 40:
        send_mail()
        print("mail sent successfully")
    else:
        print("CPU usage under limit")

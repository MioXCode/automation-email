import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_email, subject, body):
    from_email = ""
    password = ""

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    html_content = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
        </body>
    </html>
    """

    msg.attach(MIMEText(html_content, "html"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")


send_email("exmple@mail.com", "Test Email", "Python Is Best!")

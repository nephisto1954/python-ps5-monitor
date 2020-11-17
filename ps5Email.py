import smtplib

# import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

msg = EmailMessage()
msg["Subject"] = "PS5"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS

# for plain text
msg.set_content("It's available")

# for html email format
msg.add_alternative(
    """\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">It's available!</h1>
    </body>
</html>
""",
    subtype="html",
)


# # for multiple image attachments
# files = ["Screenshot.png", "Screenshoot2.png"]
# for doc in files:
#     with open(doc, "rb") as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name

#     msg.add_attachment(
#         file_data, maintype="image", subtype=file_type, filename=file_name
#     )


def send_email_alert():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, PASSWORD)
        smtp.send_message(msg)

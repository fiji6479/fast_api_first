print("fdfdf")
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
mail_conf = ConnectionConfig(
MAIL_USERNAME="testaccountruslan",
MAIL_PASSWORD="ihildpyppazpehje",
MAIL_FROM="testaccountruslan@yandex.ru",
MAIL_PORT=465,
MAIL_SERVER="smtp.yandex.ru",
MAIL_FROM_NAME="Test Messages",
USE_CREDENTIALS=True,
VALIDATE_CERTS=True,
MAIL_STARTTLS=True,
MAIL_SSL_TLS=True
)


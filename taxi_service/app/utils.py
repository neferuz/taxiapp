from twilio.rest import Client

# Здесь должны быть ваши настоящие данные
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
from_phone_number = 'your_twilio_phone_number'

client = Client(account_sid, auth_token)

def send_verification_sms(phone_number):
    verification_code = "123456"  # Пример, реально следует генерировать случайным образом
    body = f"Your verification code is {verification_code}."
    message = client.messages.create(
        to=phone_number,
        from_=from_phone_number,
        body=body
    )
    return message.sid

def verify_sms_code(phone_number, code):
    # Здесь должна быть логика проверки кода, который был отправлен пользователю
    # В реальном приложении это должно быть реализовано с проверкой временной метки и соответствующего кода
    return code == "123456"

class EmailService:
    def send_email(self, message, receiver):
        print(f"Sending {message} to {receiver} via Email")

class SmsService:
    def send_sms(self, message, receiver):
        print(f"Sending {message} to {receiver} via SMS")

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SmsService()

    def send_notification(self, message, receiver, method):
        if method == "email":
            self.email_service.send_email(message, receiver)
        elif method == "sms":
            self.sms_service.send_sms(message, receiver)

from abc import ABC, abstractmethod

class ImessageService:
    @abstractmethod
    def send(self, message, receiver):
        pass

class Email(ImessageService):
    def send(self, message, receiver):
        print("Send message via Email")

class SMS(ImessageService):
    def send(self, message, receiver):
        print("Send message via SMS")

class NotificationService:
    def __init__(self, message_service: ImessageService):
        self.message_service = message_service

    def send_notification(self, message, receiver):
        self.message_service.send(message, receiver)

sms = SMS()
ns = NotificationService(sms)
ns.send_notification("HFF", "Dfdf")
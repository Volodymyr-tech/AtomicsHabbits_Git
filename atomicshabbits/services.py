import logging
import os

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="send_message.log",
    filemode="a",
)


class SendMessageTelegram:
    def __init__(self, text, chat_id ):
        self.__TOKEN = os.getenv("TELEGRAM_TOKEN")
        self.__CHAT_ID = chat_id
        self.text = text

    def __call__(self):
        self.send_remind_message(self.text)

    def send_remind_message(self, text):
        url = f"https://api.telegram.org/bot{self.__TOKEN}/sendMessage"
        payload = {"chat_id": self.__CHAT_ID, "text": text}
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            logging.info(
                "Message was sent. Status code: %s", response.status_code
            )
            logging.info("Server response: %s", response.json())
        except requests.exceptions.RequestException as e:
            logging.error("Error occured: %s", e)

    def __str__(self):
        return (
            f"SendMessageTelegram(text={self.text}, chat_id={self.__CHAT_ID})"
        )
